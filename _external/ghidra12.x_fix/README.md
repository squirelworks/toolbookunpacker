# ghidra12.x_fix

A Win16-only patch for the Ghidra NE loader. Target is
`Ghidra_12.1.4_build`.

## Why

Ghidra 12.1.x has two bugs in its New Executable (NE) loader. They do
not affect PE, ELF, or Mach-O. They show up on ToolBook 8.0 DLLs that
have more than 127 segments, and on NE files whose entry table is not
terminated by a zero count byte.

1. **Signed segment byte.** `EntryTableBundle.type` is a Java `byte`.
   In `NeLoader.processEntryTable` the fixed-bundle path indexes the
   segment table with `bundle.getType() - 1`. A segment number of 132
   is the byte `0x84`, which Java treats as −124. The index becomes
   negative and the import throws `IndexOutOfBoundsException`. Segment
   numbers 128–253 are the broken range. `0xFF` (moveable) and `0xFE`
   (constant) are special-cased and are not the problem.

2. **Entry-table length ignored.** `EntryTable` is given `ne_cbenttab`
   as `byteCount` and never reads it. The loop stops only when it sees
   a count byte of 0. If the table is not terminated that way, the
   parser walks past it.

Windows, IDA, and Binary Ninja treat the byte as unsigned and honor
the length. The NE image is fine. The Java types are wrong.

## What the patch changes

`ne-entry-table.patch` against `Ghidra_12.1.4_build`:

- `EntryTable.java`: stop when the bytes consumed reach `byteCount`,
  as well as on a zero count.
- `NeLoader.java`: `Byte.toUnsignedInt(bundle.getType())` before the
  −1, and a bounds check that matches the moveable path.

## How to build a Linux Ghidra with this patch

Requirements on the build machine (not this sandbox):

- JDK 21 64-bit
- Git
- About 4 GB of free RAM for the build, more is better
- Network access for the Gradle wrapper

```bash
# 1. Source
git clone --depth 1 --branch Ghidra_12.1.4_build \
  https://github.com/NationalSecurityAgency/ghidra.git
cd ghidra

# 2. Patch
git apply /path/to/_external/ghidra12.x_fix/ne-entry-table.patch

# 3. Build (uses the bundled Gradle wrapper)
# Point at a real JDK 21 directory (the one that contains bin/java).
# Find it with: dirname $(dirname $(readlink -f $(which javac)))
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
./gradlew buildGhidra

# 4. Result
ls build/dist/
# ghidra_12.1.4_DEV_*.zip
```



If `git apply` says the patch is corrupt, re-download it. An earlier
copy had wrong hunk counts and spaces where the Ghidra sources use tabs.
Unzip the zip and run `./ghidraRun`. It needs JDK 21 on the machine
that launches it.

## Why a separate build

The stock Ghidra 12.1.4 binary has the bug. There is no preference or
script that turns the sign-extension off. The fix has to be in the NE
loader classes, which means a rebuild.

This is a Win16-specific change. It does not alter PE, ELF, or Mach-O
loading. Keep the stock Ghidra for everything else if you prefer; use
this build for NE files that have entry segment numbers above 127.

## This sandbox cannot build it

The environment that wrote this note has Java 17, no Gradle, and 2 GB
of RAM. Ghidra 12.1 needs JDK 21 to compile and to run, and the build
wants more memory than is available here. The patch and this README
are the deliverable. Build on a machine with JDK 21.

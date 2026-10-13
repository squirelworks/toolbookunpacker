# Ghidra and the unpacked NE

The unpacker produces an honest NE. It does not rewrite the entry
table. Ghidra 12.1.x has two bugs in its NE loader that reject some
of those honest images. The fix is a patched Ghidra, not a change to
the unpacker.

## The two bugs

Both are in the NE loader only. PE, ELF, and Mach-O are unaffected.

1. **Signed segment byte.** `EntryTableBundle.type` is a Java `byte`.
   In `NeLoader.processEntryTable` the fixed-bundle path indexes the
   segment table with `bundle.getType() - 1`. A segment number of 132
   (`0x84`) is treated as −124. The index goes negative and the import
   throws `IndexOutOfBoundsException`. Segment numbers 128–253 are the
   broken range. `0xFF` (moveable) and `0xFE` (constant) are special
   and are not the problem.

2. **Entry-table length ignored.** `EntryTable` is given `ne_cbenttab`
   as `byteCount` and never reads it. The loop stops only on a count
   byte of 0. If the table is not terminated that way, the parser
   walks past it.

Windows, IDA, and Binary Ninja treat the byte as unsigned and honor
the length. The NE image is fine.

## What the unpacker does

`unpack()` clears the self-loading flag and rewrites OPTLOADER
relocations as ordinary 8-byte NE fixups. It leaves the entry table
alone. An honest `TB80BAS.DLL` has entry segment bytes 132, 135, 136,
163, 164, 165, 180, 189, 192, and 196. Stock Ghidra 12.1.4 throws on
those. That is the loader, not the image.

## The patch

`_external/ghidra12.x_fix/ne-entry-table.patch` against
`Ghidra_12.1.4_build`:

- `EntryTable.java` stops when the bytes consumed reach `byteCount`,
  as well as on a zero count.
- `NeLoader.java` uses `Byte.toUnsignedInt(bundle.getType())` before
  the −1, and adds a bounds check that matches the moveable path.

Build steps are in `_external/ghidra12.x_fix/README.md`. The
`fetchDependencies` Gradle step is required; without it the build
stops with "Unable to find the local maven repo".

## Confirmation

The honest `TB80BAS.DLL` (1,163,488 bytes, self-loading flag clear,
entry segment bytes 132–196) was imported into a Ghidra 12.1.4 build
that had the patch applied (`ghidra_12.1.4_DEV_20261012_linux_x86_64`).
It loaded without error. The stock 12.1.4 loader throws on the same
file.

## Optional post-steps

If you cannot rebuild Ghidra, two scripts still exist as workarounds.
They are not part of `unpack()`:

- `scripts/patch_ne_entry.py` zeros the first entry-table bundle count.
  Segments load; exports are lost.
- `scripts/ghidra_cmp.py` is a CMP convenience wrapper that also
  rewrites entry segment bytes ≥ 128 to 1.

Use the patched Ghidra when you can. Use the scripts only when you
cannot.

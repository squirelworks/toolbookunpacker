# ToolBook 8.0 OPTLOADER Unpacker

Standalone Python tools for unpacking Asymetrix ToolBook 8.0 (Click2learn) 16-bit NE binaries packed with SLR OPTLOADER (1993).

These are the self-loading DLLs and EXEs (`TB80BAS.DLL`, `TB80RTM.EXE`, `TB80CMP.DLL`, etc.) that ship with the ToolBook runtime. The unpacker produces normal NE images that Ghidra, IDA, and other NE loaders can open.

## Quick start

```bash
# Unpack a single file
python3 scripts/unpack_optloader.py TB80BAS.DLL -o TB80BAS_unpacked.dll

# Unpack a directory of ToolBook binaries
python3 scripts/unpack_optloader.py /path/to/tb80/ -o unpacked/

# Prepare a CMP image that Ghidra can import (clears self-load flag, fixes entry table)
python3 scripts/ghidra_cmp.py /path/to/tb80/
```

## What it does

- Detects the OPTLOADER stamp in segment 1 and the self-loading flag. An already-unpacked image returns false from `is_optloader`.
- Expands the bitstream (literal bytes + length/distance matches) with the 16-bit wrap that the original mrcrowbar port lacked.
- Rewrites OPTLOADER relocation records as ordinary 8-byte NE fixups.
- Clears the self-loading flag (`0x0800`).
- Clears the iterated segment flag.

Segment 1 is special: it unpacks itself in place. Later segments carry their own compressed streams and custom reloc tables.

## Files

| Path | Purpose |
|------|---------|
| `scripts/unpack_optloader.py` | Main standalone unpacker (no external dependencies) |
| `scripts/optloader_mrcrowbar.py` | Older port that required mrcrowbar (kept for reference) |
| `scripts/patch_ne_entry.py` | Zero the entry-table count so Ghidra 12.x stops reading past the table |
| `scripts/ghidra_cmp.py` | Convenience wrapper for TB80CMP that also rewrites high entry segment bytes |
| `docs/FORMAT.md` | Bitstream and relocation layout |
| `docs/GHIDRA.md` | Ghidra 12.1 NE loader bugs, the patch, and the confirmation |
| `docs/SPECIMENS.md` | Packed and unpacked sizes for the binaries that were run |
| `docs/DEPENDENCY.md` | How another project imports this |
| `plannedmilestones.md` | Work that is known and not in this version |
| `examples/` | Sample command lines and the TB80RTM check |

## Ghidra import notes

Ghidra 12.1.x sign-extends the entry-table segment byte and ignores
the entry-table length. It throws `IndexOutOfBoundsException` on
ToolBook DLLs that have segment numbers > 127 in the entry table.
The unpacked image is a valid NE. The bug is in the loader.

The fix is a patched Ghidra. See `docs/GHIDRA.md` and
`_external/ghidra12.x_fix/`. The patch was confirmed: an honest
`TB80BAS.DLL` (entry segment bytes 132–196) loaded without error in
the patched 12.1.4 build.

If you cannot rebuild Ghidra, two optional post-steps remain:

1. `scripts/patch_ne_entry.py` zeros the first bundle count. Segments
   load; exports are lost.
2. `scripts/ghidra_cmp.py` is the CMP wrapper. It also rewrites entry
   segment bytes ≥ 128 to 1.

Neither is part of `unpack()`. The unpacker stays an honest NE
producer.

## Credit

This unpacker would not exist without the reverse-engineering work of **moralrecordings**:

- [mrcrowbar](https://github.com/moralrecordings/mrcrowbar) — the library that first modeled Win16 NE structures and the OPTLOADER format.
- [win16-debug](https://github.com/moralrecordings/win16-debug) — the original `optloader.py` that reverse-engineered the SLR OPTLOADER bitstream and relocation layout.

The standalone script here is a cleaned, dependency-free port of that work (with the 16-bit wrap fix for ToolBook segments). All credit for the format understanding belongs to moralrecordings.

## License

The unpacker itself is original work. The compression format is reverse-engineered from SLR OPTLOADER. Use at your own risk; the ToolBook binaries remain the property of their respective owners.

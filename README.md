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

- Detects the OPTLOADER stamp in segment 1.
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
| `docs/` | Notes on the format and known issues |
| `examples/` | Sample command lines and expected outputs |

## Ghidra import notes

Ghidra 12.1.x sign-extends the entry-table segment byte and will throw `Index -122` on ToolBook DLLs that have segment numbers > 127 in the entry table. Two workarounds:

1. Run `patch_ne_entry.py` on the unpacked DLL (zeros the first bundle count; exports are lost but segments load).
2. Use the `ghidra_cmp.py` path for CMP, or manually rewrite entry segment bytes ≥ 128 to 1 after unpacking.

The unpacked image still has a valid NE header, segment table, and relocation records.

## Credit

This unpacker would not exist without the reverse-engineering work of **moralrecordings**:

- [mrcrowbar](https://github.com/moralrecordings/mrcrowbar) — the library that first modeled Win16 NE structures and the OPTLOADER format.
- [win16-debug](https://github.com/moralrecordings/win16-debug) — the original `optloader.py` that reverse-engineered the SLR OPTLOADER bitstream and relocation layout.

The standalone script here is a cleaned, dependency-free port of that work (with the 16-bit wrap fix for ToolBook segments). All credit for the format understanding belongs to moralrecordings.

## License

The unpacker itself is original work. The compression format is reverse-engineered from SLR OPTLOADER. Use at your own risk; the ToolBook binaries remain the property of their respective owners.

# Changelog

## 1.0.0

First public form of the standalone OPTLOADER unpacker.

- Expands the SLR OPTLOADER bitstream with the 16-bit wrap on match
  copies. The wrap is the local fix for the segments the original
  mrcrowbar port rejected (TB80BAS, TB80BMP, TB80W16, and others).
- Rewrites OPTLOADER relocation records as ordinary 8-byte NE fixups.
- Clears the self-loading flag and the iterated segment flag.
- `scripts/patch_ne_entry.py` zeros the first entry-table count so
  Ghidra 12.x stops reading past the table.
- `scripts/ghidra_cmp.py` is the CMP convenience wrapper.
- `scripts/optloader_mrcrowbar.py` is the older port, kept for reference.
- Credit: the format and the original unpacker logic are from
  moralrecordings'
  [mrcrowbar](https://github.com/moralrecordings/mrcrowbar) and
  [win16-debug](https://github.com/moralrecordings/win16-debug)
  (`optloader.py`).
- Specimens and sizes are in `docs/SPECIMENS.md`.
- `is_optloader` returns false once the self-loading flag is cleared, so an already-unpacked image is not treated as packed.
- `docs/GHIDRA.md` records the two Ghidra 12.1 NE loader bugs, the
  patch in `_external/ghidra12.x_fix/`, and the 2026-10-12 confirmation
  that an honest TB80BAS.DLL loaded in the patched build.
- The unpacker stays an honest NE producer. Entry-table rewrites stay
  in the optional post-step scripts.

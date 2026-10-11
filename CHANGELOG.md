# Changelog

## 1.0.0

- Standalone OPTLOADER unpacker with 16-bit wrap on match copies.
- OPTLOADER relocation records rewritten as ordinary NE fixups.
- Self-loading flag and iterated segment flag cleared.
- `patch_ne_entry.py` for Ghidra 12.x entry-table workarounds.
- `ghidra_cmp.py` convenience wrapper for TB80CMP.
- Older mrcrowbar-based port kept as `optloader_mrcrowbar.py` for reference.

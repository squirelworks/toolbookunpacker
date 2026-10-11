# OPTLOADER format notes

## Detection

- MZ header present.
- NE header at the usual `e_lfanew` offset.
- Segment 1 contains the stamp at file offset 0x17F (relative to the segment):
  `OPTLOADER - Copyright (C) 1993 SLR Systems\nAll Rights Reserved\0`

## Bitstream

Control word is shifted left; the carry is the next bit. After 16 bits a new word is loaded.

- `1` = literal byte from the input stream.
- `0` = match. Length and distance are Elias-style bit fields. Distance is stored as a one's-complement byte pair.
- Length byte ≥ 0x82 ends the stream. 0x81 is an empty match and is skipped.

Matches are copied inside a 64 KiB window. The write cursor and the back-reference are masked to 16 bits. Without the mask the RLE copy walks off the buffer on several ToolBook DLLs (TB80BAS, TB80BMP, TB80W16, etc.).

## Segment 1

Unpacks itself. A tail of `precopy_size` bytes (read from the loader) is moved to the end of the allocation, then the bitstream is run from there. Its original NE relocation table is preserved.

## Later segments

- A word at the start of the compressed data is the relocation count.
- The bitstream follows.
- After the stream is a custom OPTLOADER relocation block that is rewritten into ordinary 8-byte NE relocation records.

## Flags cleared

- Self-loading (`0x0800` in the NE flags word).
- Iterated segment (`0x0008` in the per-segment flags).

## Known issues

- TB80ENU1 produces a short NE and is treated as suspect.
- Some modules fail the RLE copy in the older unmasked port; the 16-bit wrap fixes them.
- Entry-table segment bytes ≥ 128 cause Ghidra 12.x to throw. See `patch_ne_entry.py` and `ghidra_cmp.py`.

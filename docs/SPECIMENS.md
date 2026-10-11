# Specimens tested

These are the ToolBook 8.0 NE images the unpacker was run against.
The binaries are not in this repository. The numbers below are from
local runs on 2026-10-11.

`is_optloader` stays true after unpack because segment 1 keeps the
OPTLOADER stamp. The self-loading flag in the NE header is the field
that is cleared.

## TB80RTM.EXE

| | Packed | Unpacked |
|---|--------|----------|
| Size | 462080 | 772448 |
| SHA256 (prefix) | `2ae4d55329725349` | `7bd7c636adc3c82e` |
| NE offset | | `0xb0` |
| NE flags | | `0x030a` |
| Self-loading flag | set | cleared |
| Segments | | 139 |

## TB80BAS.DLL

| | Packed | Unpacked |
|---|--------|----------|
| Size | 683872 | 1163488 |
| SHA256 (prefix) | `ee3b2623a232bfc8` | `6b65dea3e8205d12` |
| NE offset | | `0x60` |
| NE flags | | `0x8309` |
| Self-loading flag | set | cleared |
| Segments | | 199 |

## TB80CMP.DLL

| | Packed | Unpacked |
|---|--------|----------|
| Size | 193216 | 381920 |
| SHA256 (prefix) | `ad5cfe4a43dd625e` | `d6c1a7d391f5ffa6` |
| NE offset | | `0x60` |
| NE flags | | `0x8309` |
| Self-loading flag | set | cleared |
| Segments | | 47 |

## TB80W16.DLL

| | Packed | Unpacked |
|---|--------|----------|
| Size | 76512 | 136480 |
| SHA256 (prefix) | `b73c08b90dc5e913` | `d03dcdb68df0bd67` |
| NE offset | | `0x60` |
| NE flags | | `0x8309` |
| Self-loading flag | set | cleared |
| Segments | | 56 |

## TB80BMP.DLL

| | Packed | Unpacked |
|---|--------|----------|
| Size | 68640 | 120032 |
| SHA256 (prefix) | `ede420c756e563de` | `fd3c1a27997ce54b` |
| NE offset | | `0x60` |
| NE flags | | `0x8309` |
| Self-loading flag | set | cleared |
| Segments | | 27 |

## Notes

- TB80ENU1 was previously observed to write a short NE and is treated as
  suspect. It is not in the table above.
- Entry-table segment bytes ≥ 128 are a Ghidra 12.x problem, not an
  unpacker problem. See `scripts/patch_ne_entry.py` and
  `scripts/ghidra_cmp.py`.

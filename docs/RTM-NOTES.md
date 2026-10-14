# RTM notes

Date: 2026-10-14

TB80RTM.EXE is a 16-bit NE. Unpacked image is at `artifacts/Toolbook/_unpacked/TB80RTM.EXE`.

Decompile is 163173 lines, 134 segments.

## Named functions

| Function | Role |
|----------|------|
| `FUN_1068_0098` | `GLOBALALLOC` with retry on OOM |
| `FUN_1068_00d0` | OOM dialog, returns 4 to retry |
| `FUN_1068_0000` | dialog helper |
| `FUN_10d0_3166` | window long reader |

## Thin wrappers

| API | Functions |
|-----|-----------|
| `BEGINPAINT` | `FUN_1070_0be0`, `FUN_1098_14fc`, `FUN_1120_06da` |
| `ENDPAINT` | `FUN_1070_0be0`, `FUN_1120_06da` |
| `CREATEWINDOW` | `FUN_1050_08aa`, `FUN_10a8_0062`, `FUN_10a8_1c3c` |
| `DESTROYWINDOW` | `FUN_1050_1566`, `FUN_1050_196a` |
| `SHOWWINDOW` | `FUN_1098_1b88`, `FUN_10d0_3166`, `FUN_1188_25ac` |
| `ENABLEWINDOW` | `FUN_10b8_33f0`, `FUN_1188_25ac`, `FUN_1188_267a` |
| `SETFOCUS` | `FUN_1060_0b80`, `FUN_1098_1ca0`, `FUN_10b8_33f0` |
| `GETFOCUS` | `FUN_1060_0a48`, `FUN_1060_0b80`, `FUN_1098_0d44` |
| `INVALIDATERECT` | `FUN_1010_0376`, `FUN_1070_063a`, `FUN_1070_07fa` |
| `ENDDIALOG` | `FUN_1188_2450`, `FUN_1188_2b8e` |

## API counts

| API | Hits |
|-----|------|
| `GETDLGITEM` | 446 |
| `SENDMESSAGE` | 321 |
| `LSTRLEN` | 282 |
| `GLOBALUNLOCK` | 275 |
| `GETWINDOWLONG` | 275 |
| `GLOBALLOCK` | 210 |
| `GLOBALFREE` | 205 |

## GETDLGITEM control IDs

| ID | Count |
|----|-------|
| 0x65 (101) | 55 |
| 0x67 (103) | 12 |
| 0xDB8 (3512) | 12 |
| 0x11E3 (4579) | 10 |

## GETWINDOWLONG indices

| Index | Count |
|-------|-------|
| 10 | 196 |
| 8 | 35 |
| 0xFFF0 (-16) | 30 |
| 0xFFFC (-4) | 2 |
| 0 | 1 |

## Not the record reader

No named file open. Named CDB functions: `CDBSAVEBOOK`, `CDBGETVALUEEX`, `CDBSENDVALUEEX`, `CDBSETVALUEEX`. These are the property bus.

# RTM notes

Date: 2026-10-14

TB80RTM.EXE is a 16-bit NE. Unpacked image is at `artifacts/Toolbook/_unpacked/TB80RTM.EXE`.

Decompile is 163173 lines, 134 segments. Top named tokens: `GETDLGITEM` (446), `SENDMESSAGE` (321), `LSTRLEN` (282), `GLOBALUNLOCK` (275), `GETWINDOWLONG` (275).

No named file open (`_lopen`, `_lread`, `OpenFile`, `ReadFile`, `CreateFile`). Named CDB functions: `CDBSAVEBOOK`, `CDBGETVALUEEX`, `CDBSENDVALUEEX`, `CDBSETVALUEEX`.

Thin wrappers for `BEGINPAINT`, `ENDPAINT`, `CREATEWINDOW`, `DESTROYWINDOW`, `SHOWWINDOW`, `ENABLEWINDOW`, `SETFOCUS`, `GETFOCUS`, `INVALIDATERECT`, `ENDDIALOG`.

Full notes: `tbworkingpapers/tbwp0018/rtm-triage.md`, `tbworkingpapers/tbwp0018/rtm-nameable.md`.

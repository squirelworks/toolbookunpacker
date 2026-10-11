# Planned milestones

Not bugs. Work that is known and not in the current unpacker.

## v1.x

- Confirm TB80ENU1. The older port wrote a short NE; decide whether the
  current standalone script handles it or whether it stays out of scope.
- Add a one-line verification note for each new specimen in
  `docs/SPECIMENS.md` when a consumer reports a size or flag mismatch.
- Keep the entry-table workaround (`patch_ne_entry.py`, `ghidra_cmp.py`)
  until Ghidra's NE loader stops sign-extending the segment byte.

## Later

- Optional: a tiny synthetic OPTLOADER fixture so a consumer can run a
  check without a ToolBook binary. Not required for the first release.
- Optional: GitHub Actions that run that fixture on push. See the
  conversation note on CI.

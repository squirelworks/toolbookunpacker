# Test records

Each `test_<name>_<timestamp>.txt` is one run of the unpacker against a
private ToolBook binary. The binary is not in this repository. The record
lists the packed size, SHA256, NE header, and the same fields after unpack,
plus whether the self-loading flag was cleared.

`summary_<timestamp>.txt` is the table for that run.

Run `20261011_124845` covered 21 OPTLOADER images. All unpacked. The
self-loading flag was cleared on every one. Ten other ToolBook files in
the same directory were not OPTLOADER and were skipped.

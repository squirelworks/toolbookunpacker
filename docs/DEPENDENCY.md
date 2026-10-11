# Using this from another project

This repository is meant to be a submodule or a vendored tree, not a
pip package. Other ToolBook work (TBpipeline, decompiler chats) should
depend on it rather than carry their own copy of the unpacker.

## Import

Add `scripts/` to `sys.path`, then import the public names.

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path("toolbookunpacker/scripts").resolve()))
from unpack_optloader import is_optloader, unpack

data = open("TB80BAS.DLL", "rb").read()
if is_optloader(data):
    image = unpack(data)
    open("TB80BAS_unpacked.dll", "wb").write(image)
```

`unpack()` returns the complete NE image with the self-loading flag
cleared and OPTLOADER relocations rewritten as ordinary NE fixups.

`ghidra_cmp.py` uses the same import. It adds its own directory to
`sys.path` when run as a script, so either of these works:

```bash
python3 toolbookunpacker/scripts/ghidra_cmp.py /path/to/tb80/
python3 -c "import sys; sys.path.insert(0, 'toolbookunpacker/scripts'); import ghidra_cmp"
```

## Ghidra path

For modules that Ghidra 12.x rejects because of high entry-table
segment bytes, use `patch_ne_entry.py` or the CMP-specific
`ghidra_cmp.py`.

## Credit

Format understanding and the original unpacker logic come from
moralrecordings' mrcrowbar and win16-debug projects.

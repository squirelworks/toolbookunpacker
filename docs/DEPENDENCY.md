# Using this as a dependency

Other ToolBook projects (TBpipeline, decompiler chats, Foolbook tooling) should depend on this repository rather than carrying their own copy of the unpacker.

## Vendoring

Copy the `scripts/` directory (or the whole tree) into the consumer and add it to `sys.path`, or install it as an editable package.

## Expected interface

```python
from unpack_optloader import is_optloader, unpack

data = open("TB80BAS.DLL", "rb").read()
if is_optloader(data):
    image = unpack(data)
    open("TB80BAS_unpacked.dll", "wb").write(image)
```

`unpack()` returns the complete NE image with the self-loading flag cleared and OPTLOADER relocations rewritten as ordinary NE fixups.

## Ghidra path

For modules that Ghidra 12.x rejects because of high entry-table segment bytes, use `patch_ne_entry.py` or the CMP-specific `ghidra_cmp.py`.


## Credit

Format understanding and the original unpacker logic come from moralrecordings' mrcrowbar and win16-debug projects.

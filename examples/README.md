# Examples

```bash
# From the repository root
python3 scripts/unpack_optloader.py TB80RTM.EXE
# writes TB80RTM_unpacked.exe

python3 scripts/unpack_optloader.py TB80BAS.DLL TB80BMP.DLL TB80W16.DLL -o unpacked/
# writes one unpacked image per input into the unpacked/ directory

# Ghidra-friendly CMP
python3 scripts/ghidra_cmp.py .
# looks for TB80CMP.DLL and writes TB80CMP.ghidra.dll
```

The unpacked images are ordinary NE files. The self-loading flag is cleared, so Windows will not call the OPTLOADER stub.

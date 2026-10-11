#!/usr/bin/env python3
"""Convenience entry point. Forwards to scripts/unpack_optloader.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "scripts"))
from unpack_optloader import main

if __name__ == "__main__":
    sys.exit(main())

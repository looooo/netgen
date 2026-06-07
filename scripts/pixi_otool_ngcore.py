#!/usr/bin/env python3
"""Run otool -L on libngcore.dylib and pyngcore*.so (macOS only; no-op elsewhere)."""
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if sys.platform != "darwin":
        print("otool-ngcore: skipped (not macOS)")
        return 0

    prefix = os.environ.get("CONDA_PREFIX") or os.environ.get("PIXI_ENV_PREFIX")
    if not prefix:
        print("otool-ngcore: CONDA_PREFIX or PIXI_ENV_PREFIX not set", file=sys.stderr)
        return 1

    lib = Path(prefix) / "lib" / "libngcore.dylib"
    if not lib.is_file():
        print(f"otool-ngcore: missing {lib}", file=sys.stderr)
        return 1

    print("===", lib)
    subprocess.run(["otool", "-L", str(lib)], check=True)

    import pyngcore  # noqa: PLC0415 — after install

    d = Path(pyngcore.__file__).parent
    sos = sorted(d.glob("pyngcore*.so"))
    if not sos:
        print(f"otool-ngcore: no pyngcore*.so under {d}", file=sys.stderr)
        return 1
    for so in sos:
        print("===", so)
        subprocess.run(["otool", "-L", str(so)], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

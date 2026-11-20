"""Package the verified production SPV binary; exclude test-only contracts."""

import argparse
import hashlib
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_commit")
    parser.add_argument("build_image")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.source_commit):
        parser.error("expected a full source commit SHA")
    if not re.fullmatch(r"[^\s@]+@sha256:[0-9a-f]{64}", args.build_image):
        parser.error("expected a pinned build image digest")

    name = "ckb-bitcoin-spv-type-lock"
    binary = (Path("build/release") / name).read_bytes()
    if not binary.startswith(b"\x7fELF"):
        raise SystemExit(f"{name}: expected an ELF binary")
    sha256 = hashlib.sha256(binary).hexdigest()
    ckb_data_hash = hashlib.blake2b(
        binary, digest_size=32, person=b"ckb-default-hash"
    ).hexdigest()
    manifest = {
        "schema_version": 1,
        "source_commit": args.source_commit,
        "build_image": args.build_image,
        "contracts": [
            {
                "name": name,
                "size_bytes": len(binary),
                "sha256": sha256,
                "ckb_data_hash": "0x" + ckb_data_hash,
            }
        ],
    }
    args.output.mkdir(parents=True)
    (args.output / name).write_bytes(binary)
    (args.output / "SHA256SUMS").write_text(f"{sha256}  {name}\n", encoding="utf-8")
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

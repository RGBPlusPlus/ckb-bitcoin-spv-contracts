# CKB Bitcoin SPV Contracts

[![License]](#license)
[![GitHub Actions]](https://github.com/ckb-cell/ckb-bitcoin-spv-contracts/actions)

> [!WARNING]
> This repository is still in the proof-of-concept stage.

[Bitcoin] SPV clients in [CKB] contracts.

[License]: https://img.shields.io/badge/License-MIT-blue.svg
[GitHub Actions]: https://github.com/ckb-cell/ckb-bitcoin-spv-contracts/workflows/CI/badge.svg

## Contracts

- [A type script for Bitcoin SPV clients.](contracts/ckb-bitcoin-spv-type-lock)

- For testing purpose only:

  - ["Can Update Without Ownership" Lock](contracts/can-update-without-ownership-lock)

## Audit Report

An audit report has been conducted to ensure the security and functionality of the contracts. You can find the detailed report [here](./CKB%20Bitcoin%20SPV%20Contracts%20Audit%20Report.pdf).


## License

Licensed under [MIT License].

[Bitcoin]: https://bitcoin.org
[CKB]: https://github.com/nervosnetwork/ckb

[MIT License]: LICENSE

### Contract build artifacts

The **Checksum** workflow uses the pinned Docker image and checks the build
against `checksums.txt`. Download `contract-binaries-<commit>` from a successful
run to get the production `ckb-bitcoin-spv-type-lock` binary. The bundle includes
`SHA256SUMS` (verify with `sha256sum -c SHA256SUMS`) and `manifest.json` with
the source commit, build image digest, byte length, SHA-256, and CKB data hash.
The test-only lock is checked by CI but is not packaged.

To publish these same files to GitHub Releases, configure a tag ruleset for
`v*` that restricts creation to release maintainers and prevents tag updates
and deletion, then push a `vMAJOR.MINOR.PATCH` tag for a commit on the default
branch. Add a suffix such as `-rc.1` to publish a prerelease. A tagged build
must also pass the existing CKB-VM tests against the exact release binaries.
Unprotected tags do not publish. This builds and distributes binaries only;
it does not deploy any contract.

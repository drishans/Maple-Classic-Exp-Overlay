# Where the download comes from

Downloads on the [Releases page](https://github.com/drishans/Maple-Classic-Exp-Overlay/releases) are built by GitHub from the code in this repository ([Build workflow](../.github/workflows/build.yml)), not on anyone's own PC. Each build:

- installs exact package files, each checked against its SHA-256 ([requirements-build.txt](../requirements-build.txt)),
- runs the tests, including the [offline check](../tests/test_offline.py),
- records a signed **attestation**: which workflow built which file, from which commit,
- puts each file's **SHA-256** on the release page (`SHA256SUMS.txt`).

**Check your download** with the free [GitHub CLI](https://cli.github.com):

```
gh attestation verify "the file you downloaded" --repo drishans/Maple-Classic-Exp-Overlay
```

It tells you whether that exact file was built here, and from which commit. Or compare the file's SHA-256 with `SHA256SUMS.txt` on its release page (in PowerShell: `Get-FileHash "the file you downloaded"`; on a Mac, in Terminal: `shasum -a 256 "the file you downloaded"`).

The same files are also kept on the page of the build that made them (Actions, the run, the file at the bottom; you need a GitHub account to download it).

The original overlay's downloads are on [beanguri's Releases page](https://github.com/beanguri/Maple-Classic-Exp-Overlay/releases), checked the same way with `--repo beanguri/Maple-Classic-Exp-Overlay`. They are a different program from this one: they can share runs and send reports if you agree.

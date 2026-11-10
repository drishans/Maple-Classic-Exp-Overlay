"""The offline fork's promise, checked in the source: the program never goes online by itself, never opens a
handle to another process, and never sends input. Reads the files only (nothing is run), so it needs no game,
screen or packages, and it fails loudly when a merge from upstream brings any of that back.

Run from the project folder:  python tests/test_offline.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# What the download is made of: the program's own modules. Build and release scripts and tools/ run only on a
# developer's PC or on GitHub, never in the player's copy.
NOT_SHIPPED = {"build.py", "build_macos.py", "check_macos.py", "release_plan.py"}
SHIPPED = sorted([p for p in ROOT.glob("*.py") if p.name not in NOT_SHIPPED] + list((ROOT / "platforms").glob("*.py")))

FORBIDDEN = {
    "the network": r"\burllib\.request\b|\burlopen\b|\bhttp\.client\b|^\s*(import|from)\s+(socket|http|requests|"
                   r"httpx|aiohttp|ftplib|smtplib|xmlrpc)\b|\bsocket\.",
    "another process's handle or memory": r"\bOpenProcess\b|\bReadProcessMemory\b|\bWriteProcessMemory\b|"
                                          r"\bVirtualAllocEx\b|\bCreateRemoteThread\b|\bDebugActiveProcess\b",
    "sending input or hooking it": r"\bSendInput\b|\bkeybd_event\b|\bmouse_event\b|\bSetWindowsHookEx\w*\b|"
                                   r"\bPostMessage\w*\b|\bSendMessage\w*\b|\bCGEventPost\b",
}

failures = 0


def check(name, ok):
    global failures
    print(("PASS " if ok else "FAIL ") + name)
    failures += not ok


check("the program's own modules are found (the scan isn't empty)",
      len(SHIPPED) > 15 and any(p.name == "maple_exp.py" for p in SHIPPED)
      and any(p.parent.name == "platforms" for p in SHIPPED))
for what, pattern in FORBIDDEN.items():
    found = []
    for path in SHIPPED:
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            code = line.split("#", 1)[0]                    # (a comment may name what isn't done)
            if re.search(pattern, code):
                found.append(f"{path.relative_to(ROOT)}:{n}: {line.strip()[:100]}")
    check(f"nothing in the program uses {what}" + (":\n    " + "\n    ".join(found) if found else ""), not found)

main = (ROOT / "maple_exp.py").read_text(encoding="utf-8")
for name in ("post_runs", "post_health", "post_report", "check_for_update", "share_runs", "sharing_blocked"):
    check(f"maple_exp.py has no {name}", not re.search(rf"\b{name}\b", main))
check("the server folder (upstream's website) isn't part of the fork", not (ROOT / "server").exists())
check("the daily health report module is gone", not (ROOT / "healthlog.py").exists())

print(f"\n{failures} failure(s)" if failures else "\nall passed")
sys.exit(1 if failures else 0)

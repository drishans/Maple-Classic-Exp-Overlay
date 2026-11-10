# For developers

**Run from source.** You need Python 3.10 or newer, and [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) for map names.

```
py -3 -m pip install -r requirements.txt
run.bat
```

**From source on macOS:** `brew install tesseract`, then `python3 -m pip install -r requirements.txt` and `python3 maple_exp.py`. Allow your Terminal (or Python) in Screen Recording instead of the app.

Everything that differs between Windows and macOS (finding the game window, screen scaling, hotkeys, the one-copy-at-a-time lock) is in `platforms/`: one `Platform` interface in `base.py`, one implementation per OS, and `create_platform()` picks the one for the OS it's on.

**Build the download** (puts `Maple-Classic-Exp-Overlay-v<version>.zip` in `release/`, and a copy to use right away in the project folder: `Maple Classic Exp Overlay.exe` with its `_internal` folder):

```
py -3 -m pip install -r requirements.txt pyinstaller
py -3 build.py
```

**The Mac download** is built by `build_macos.py` on a Mac (Apple Silicon or Intel, for the Mac it runs on); how to use it is at the top of that file. `check_macos.py` checks the result.

**Run the tests:**

```
py -3 tests/test_offline.py   # reads the source only: nothing goes online, no other process, no input
py -3 tests/test_logic.py
py -3 tests/test_screen.py
py -3 tests/test_ui.py        # opens the real window for a few seconds (the notes box)
```

To build with exactly the packages the releases use: `py -3 -m pip install --require-hashes -r requirements-build.txt`.

GitHub runs the tests on every push ([Tests workflow](../.github/workflows/tests.yml)). The [Build workflow](../.github/workflows/build.yml) builds the download on GitHub (Actions tab, **Build**, **Run workflow**) and runs the tests first. Pushing a version tag (`v` + `VERSION` in `maple_exp.py`, like `v0.9.16-offline.1`) also attests the files and drafts the release with them; releases are only ever made that way.

**How it reads the screen:**
- It finds the game window by its window class (`MapleStoryClass`), then the EXP numbers (like `12,345 [12.34%]`) in the status bar. It never opens a handle to the game's process.
- Each digit is resized to a standard size and compared against saved examples of the game's font in `assets/`.
- A reading only counts if the EXP and % agree with how much EXP that level needs, so misreads are ignored.
- Mesos are read the same way. The mesos box is found by its outline, which also works while the inventory is see-through.
- The potion counts, your level (the orange **LV** badge) and the EXP number are read with the game's own font, drawn from `assets/fonts_v2/`; the party size by the exact shape of the party list's HP bars (`assets/party_shapes.json`). The older EXP reader and party count stay as a backup. Mesos are still read the older way; a newer mesos reader runs in a test mode that only compares and never changes a number you see.
- The party size is the number of HP bars in the party list.
- Map names are read with Tesseract, and matched to the game's list in `assets/maps.txt` (made by `tools/make_maps.py`).
- Settings, the log and `errors.log` are saved in `%APPDATA%\MapleEXP` (`~/Library/Application Support/MapleEXP` on macOS; from its old name, Maple EXP/hr, so updates keep them).

## This fork and upstream

This is a fork of [beanguri/Maple-Classic-Exp-Overlay](https://github.com/beanguri/Maple-Classic-Exp-Overlay) (MIT). What's different:

- **No network code.** The update check, run sharing (`post_runs`), daily health reports (`healthlog.py`, `post_health`) and Send to the developer (`post_report`) are removed, with their settings and first-run questions. Best maps, Releases and Report a bug only open the browser.
- **No process handle.** The game window is matched by its class alone (upstream also asked Windows for the program name with `OpenProcess`).
- **No `server/`.** That's upstream's mcwo.app site. `tools/make_maps.py` (from `server/tools/`) now only writes `assets/maps.txt`.
- **Its own version numbers** (`0.9.16-offline.1` is upstream 0.9.16-beta plus this fork's changes), so it's never taken for an upstream release.

**Taking upstream's reader fixes:** the remote is `upstream`.

```
git fetch upstream
git merge upstream/main
py -3 tests/test_offline.py
```

Conflicts will mostly be in `maple_exp.py`'s `App` class (Settings, first run, the queue pump) and in `report.py`. Keep this fork's side for anything that sends; take upstream's side for the readers. `test_offline.py` fails if a merge brings back network code, a process handle or input.

Please don't point anything at mcwo.app other than the Best maps link: upstream's site only takes data from upstream's own releases.

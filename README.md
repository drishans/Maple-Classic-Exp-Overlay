<h1><img src="docs/icon.png" width="40" align="top"> Maple Classic Exp Overlay (offline fork)</h1>

**An EXP tracker for MapleStory Classic World that never goes online.** A small window sits next to the game and shows how fast you're leveling and making mesos.

This is a fork of [beanguri's Maple Classic Exp Overlay](https://github.com/beanguri/Maple-Classic-Exp-Overlay) with every network feature taken out: no update check, no run sharing, no health reports, no "Send to the developer". It also never opens a handle to the game's process. The screen reading, the log, compact mode, potions and net mesos are all beanguri's work.

**[Download it here](../../releases/latest)** · [How to install](#how-to-install) · [What's different](#whats-different-from-the-original)

![The overlay next to MapleStory, while farming](docs/screenshot-game.jpg)

## What it shows

![The overlay up close, with its log open](docs/screenshot-main.png)

- **EXP per hour**, for your whole session and for the last 5 minutes, and how long until your next level
- **Mesos per hour**, read from your inventory, and **net mesos per hour** (minus what your potions cost)
- **A log of every map you farm**: EXP/hr and mesos/hr there, at which level and class, solo or in a party

You don't type anything in. It reads all of this from your game screen by itself.

## What's different from the original

| | Original | This fork |
|---|---|---|
| Update check at start | Yes (can be turned off) | No. Settings > **Releases** opens the download page in your browser |
| Share 15-minute runs with mcwo.app | If you say yes | Never |
| Daily health report | If you say yes | Never |
| Report a bug | GitHub, or send straight to the developer | GitHub only, submitted by you in your browser |
| Finding the game window | Window class, or title plus the game's program name (asks Windows about the game's process) | Window class only (never touches the game's process) |
| Potions no NPC sells (Mana Elixir, Power Elixir...) | Counted as free until you type a price | Net mesos/hr asks for a price instead of counting them as free. **Look up** next to each one opens its Free Market price on [maplestory.watch](https://maplestory.watch) in your browser; type 0 for one you only loot |
| Everything else | | The same |

A test ([tests/test_offline.py](tests/test_offline.py)) checks the source on every build: it fails if any network code, process handle or input sending comes back.

## How to install

### On Windows (10 or 11)

1. Go to the **[download page](../../releases/latest)** and, under **Assets**, click the **Maple-Classic-Exp-Overlay-v….zip** file. (Not "Source code".)
2. **Right-click** the zip in your Downloads folder, choose **Extract All...**, then **Extract**. Double-clicking it isn't enough.
3. Open the new folder, then **Maple Classic Exp Overlay** inside it, and double-click **Maple Classic Exp Overlay.exe**.

**"Windows protected your PC"?** Click **More info**, then **Run anyway**. Windows shows this for any program that isn't signed.

**Keep the whole folder together:** the program needs the files next to it. To put it on your desktop, right-click the .exe and choose **Send to > Desktop (create shortcut)** (on Windows 11, under **Show more options**).

**Already using the original?** Close it first (only one can run at a time). Your log, notes and settings carry over: both use the same data folder.

### On macOS

The Mac build works the same way as the original's: pick the `.dmg` for your Mac (Apple Silicon or Intel, macOS 14 or newer), drag the app to Applications, allow it under **System Settings > Privacy & Security** (it isn't signed by Apple), and allow it under **Screen Recording**. The Mac version came from thanhphamvan's, fabriciorby's and cpaez33's work on the original. Hotkeys aren't available on macOS yet.

## How to use it

1. **Start MapleStory**, then the overlay. It finds the game window by itself.
2. **Don't cover** the minimap, the EXP bar, the mesos at the bottom of your inventory or the party list with the overlay. It tells you if it's in the way.
3. **Press Start** and play. It pauses by itself after 15 seconds without EXP or when you leave the map, and carries on at your next EXP. A new map starts new numbers (unless **No Reset** is on).
4. **For mesos,** open your inventory when you start and now and then. **For net mesos,** keep your potions on the quick-slot bar.

| Control | What it does |
|---|---|
| **Start / Pause** | Starts and stops tracking |
| **Reset** (round arrow) | Starts over from zero |
| **Log this run** | Turn it off to keep this run out of the log. It turns itself back on after the run. |
| **No Reset** | For farming across maps: changing maps doesn't start new numbers. |
| **Best maps** | Opens [mcwo.app](https://mcwo.app), the original author's best-maps site, in your browser, for your level, party size and class |
| **...** (More) | **View capture** shows what it read; **Select area** if it can't find the EXP numbers |
| Log, compact and ⚙ icons | The log, a smaller window (Square, Wide or Bar), and Settings |

Hotkeys (Windows): **Shift+1** Start/Pause, **Shift+2** Reset, **Shift+3** Log this run, **Shift+4** Compact. Change them in ⚙.

**More:** the [full guide](docs/guide.md) has the log, compact shapes, hotkeys, every setting, net mesos and potions, and how accurate it is.

## Something not working?

**Click View capture first** (in **...**). It shows exactly what the overlay read.

| Problem | Try this |
|---|---|
| An error when you open the .exe | Extract the zip first (step 2). It can't run from inside the zip or away from its folder. |
| "MapleStory window not found" | Start the game first, and bring it back up if it's minimized. If it still isn't found, use **Select area** (in **...**). |
| "Can't find the EXP bar" | Make sure nothing covers the bottom of the game, the overlay included. A very small game window: make it bigger. |
| Mesos says "open inventory" | Open your inventory and make sure the mesos at its bottom aren't covered (in small windows the chat bar can). |
| The map name is wrong | Right-click the log line, **Rename map**. |
| Anything else | ⚙ > **Report a bug** opens a GitHub issue in your browser, filled in with what the overlay read. |

More fixes: [the full guide](docs/guide.md#something-not-working).

## Is it safe? Is it allowed?

- **Only download it from this repository's [Releases](../../releases)** (or the original from [beanguri's](https://github.com/beanguri/Maple-Classic-Exp-Overlay/releases)). Copies from anywhere else haven't been checked by anyone. Downloads here are built by GitHub, and you can [check that](docs/download.md).
- **It only looks at your screen**, like a screen recorder. It never touches the game's files, memory or process, and never presses keys or clicks for you.
- **It never goes online by itself.** Your log, notes, settings and potion data stay on your PC. Details: [Privacy](docs/privacy.md).
- **Your antivirus might warn about it** by mistake. All of the code is public right here, so anyone can check what it does.
- **It isn't made or approved by Nexon.** Nexon's terms forbid unauthorized third-party software, and the game's anti-cheat can see which programs are running. Nobody outside Nexon knows how it treats screen-reading tools like this one, and taking out the network code doesn't change that. You use it at your own risk: if your account matters to you, the safest choice is not to run it.

## Updates

This copy never checks for updates. To see if there's a newer one, click ⚙ > **Releases**, which opens the [download page](../../releases/latest). Download the new version and use it instead of the old one: your log, notes and settings stay.

## More

- [Full guide](docs/guide.md) · [Privacy](docs/privacy.md) · [Where the download comes from](docs/download.md) · [For developers](docs/developers.md) (run from source, build, tests, taking fixes from upstream)
- Credits: the overlay is [beanguri's](https://github.com/beanguri/Maple-Classic-Exp-Overlay), with contributions from its community; [CHANGELOG.md](CHANGELOG.md) is its history up to the fork. The [EXP table](https://meowdb.com/msclassic/guides/exp-table-level-1-to-100) (used to work out your level) and the [list of map names](https://meowdb.com/msclassic/maps/all) (`assets/maps.txt`) are from meowdb, a fan-made MapleStory Classic database. Map names are read with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (Apache 2.0 license), included in the download. The typeface is [Manrope](https://github.com/googlefonts/manrope) (SIL Open Font License, `assets/fonts/OFL.txt`).
- License: [MIT](LICENSE), from the original. Free to use, change and share.

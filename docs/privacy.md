# Privacy

**This copy never goes online by itself.** There's no update check, no run sharing, no daily health report and no "Send to the developer". The program has no code that opens a network connection, and a test ([test_offline.py](../tests/test_offline.py)) fails the build if any comes back.

What it keeps, and the only times anything leaves your PC:

- **Your log, your notes and your settings stay on your PC**, in `%APPDATA%\MapleEXP` (`~/Library/Application Support/MapleEXP` on a Mac). It's the same folder the original overlay uses, so you can switch between them and keep your log. One thing to know: if you go back to the original overlay with its run sharing on, it can share the 15-minute runs this copy logged, because they're in the same log.
- **A copy of your log is kept for each day** (the last 7 days), in the `backups` folder next to it, so if anything ever goes wrong there's a recent one. To go back to one, close the overlay and copy it over `exp_log.json`.
- **Potions stay here too.** Your potion counts, prices and costs are never sent anywhere.
- **Buttons that open your browser** only do it when you click them, and then it's your browser that goes online, not the overlay:
  - **Best maps** opens [mcwo.app](https://mcwo.app) (the original author's site) with your level, party size and class in the address, so that site sees them.
  - **Releases** opens this fork's download page on GitHub.
  - **Report a bug** opens a new GitHub issue, filled in with your version and what the overlay was reading (file paths cut down to the file name, and your Windows or Mac user name and computer name taken out). Nothing is sent until you click Submit there yourself. It also saves `bug-report.png` and `bug-report.txt` for you to drag in, and, only if you say yes, a picture of the whole game window (which can show chat and names). That picture is deleted after 5 minutes.

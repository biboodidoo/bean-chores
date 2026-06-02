# Bean's Chore Quest 🦊

A simple, gamified chore tracker for Bean — a free, no-subscription alternative to the Skylight calendar.

It runs two ways from the **same** `index.html`:
- **Solo (default):** open the file or the hosted link — data lives per-device in the browser, nothing sent anywhere.
- **Family sync (recommended):** run the little server on your Mac and every device on your home Wi-Fi shares ONE board. No internet, no accounts, no cloud.

---

## 🏠 Run it on your home network (multi-device sync)

This is the setup where Bean's iPad, your phone, and your husband's phone all see the same stars and streak, fully offline.

**Start the server (on your Mac):**
- Double-click **`Start Bean Chores.command`** in this folder. A Terminal window opens and prints the links to use. Keep that window open while the family is using the app.
  - (The very first time, macOS may ask "Do you want python3 to accept incoming network connections?" — click **Allow**. You may also need to right-click → Open the first time, since it's an unsigned script.)
- Or from Terminal: `cd` into this folder and run `python3 server.py`.

**Open it on each device (same Wi-Fi):**
1. In Safari/Chrome go to `http://<your-mac-name>.local:8080` (the start window prints the exact address, e.g. `http://OSXLAP10947.local:8080`, with the IP address as a backup).
2. Tap **Share → Add to Home Screen** for a full-screen, app-like icon.
3. Everyone's now on the same board. A change on one device shows on the others within ~2 seconds.

**Notes:**
- The board is live only while your Mac is awake and running the server. When the Mac is off or away, devices just wait — progress is safe and resumes when it's back.
- All data lives in `data.json` in this folder (the single source of truth). The server snapshots it into `backups/` on every change (keeps the latest 30).
- Later you can move the server to an always-on box (e.g. a spare iPhone SE / small computer) so it's up 24/7.

---

## How to use it (solo / per-device)

**On a laptop:** double-click `index.html` — it opens in your browser. That's it.

**On a tablet or phone (the Skylight-style setup):**
1. Email yourself `index.html`, or drop it in iCloud/OneDrive and open it on the tablet.
2. Open it in Safari (iPad) or Chrome (Android).
3. Tap the Share button → **Add to Home Screen**. It now launches full-screen like a real app, with the fox icon.
4. Mount the tablet on the fridge or wall and you've got your chore board.

> Tip: keep a cheap tablet on a stand in the kitchen — that's the whole Skylight pitch, minus the $160 device and the subscription.

## What it does

- **Quests** — Bean taps a chore to complete it, earns ⭐ stars, and gets confetti + a happy sound.
- **Swipe to skip** — swipe a quest card to the right to remove it *just for today* (e.g. no viola on a school holiday). It comes back automatically tomorrow, and a "tap to undo" toast appears in case of a mis-swipe.
- **Levels** — stars build toward levels (Sprout → Explorer → … → Mythic) with a progress bar.
- **Streaks** — a 🔥 day-streak rewards doing at least one quest every day.
- **Reward Shop** — Bean spends stars on real-life rewards you define (screen time, ice cream, movie night…). Rewards lock until there are enough stars.
- **Progress tab** — all-time stars, chores completed, best streak, rewards claimed.
- **Daily reset** — quests automatically reset each morning so they can be done again.

## Parent settings (⚙️ gear, top-right) — PIN protected 🔒

The first time you tap the gear (or the avatar), you'll be asked to **create a parent PIN**. After that, the PIN is required every time, so Bean can't add her own chores or claim settings. You can change it anytime via **🔒 Change parent PIN**. Forgot it? Clearing the browser's site data resets everything.

Inside settings you can:

- Change Bean's name and avatar.
- Add / edit / delete chores and their star values.
- **Add an ad-hoc "Just for today" task** — flip the *Just for today ✨* toggle when adding a chore. It shows a blue "today" badge and disappears automatically at the next daily reset (great for one-off jobs like "help carry groceries").
- Add / edit / delete rewards and their star costs.
- Reset today's quests manually.
- Erase everything and start over.

Tapping a completed quest again **un-checks it** and refunds the stars, in case of a mis-tap.

## Notes

- Data is stored per-device in `localStorage`. Two different devices keep separate progress; clearing the browser's site data wipes it.
- The only network request is the Google font — it still works fine offline (falls back to a system font).
- Want it on multiple kids' devices in sync? That would need a small backend — say the word and it can be added.

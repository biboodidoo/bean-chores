# Bean's Chore Quest 🦊

A simple, gamified chore tracker for Bean — a free, no-subscription alternative to the Skylight calendar.
It's a single self-contained HTML file: no install, no account, no backend, works offline. Data lives in the browser on the device, nothing is sent anywhere.

## How to use it

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

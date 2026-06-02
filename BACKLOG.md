# Bean's Chore Quest — Backlog

Running list of requests, feature ideas, issues, and decisions. Captured 2026-06-01.

- **App source:** `bean-chores/index.html` (single self-contained file)
- **Live (temporary, public) demo:** https://biboodidoo.github.io/bean-chores/
- **Repo:** github.com/biboodidoo/bean-chores

---

## 🔨 To build / tackle next session

1. ✅ **DONE (2026-06-02) — Show today's date next to the streak.** Uses device system time, e.g. `🔥 0 day streak · Tue, Jun 2`.

2. **LAN-synced, offline backend — the big one. ← NEXT UP** (Task `child-001`)
   - Self-hosted family chore board synced across Yiyao's phone, husband's phone, and Bean's iPad over home Wi-Fi. No internet.
   - One shared source of truth (everyone sees the same stars/streak). Swap per-device `localStorage` for a shared server + database with polling/near-real-time sync.
   - **Host on Yiyao's laptop to start** (on most of the time; OK for the board to pause when laptop is off or she's away).
   - **Later:** graduate to an always-on box (spare iPhone SE).
   - Single child only (no siblings). Parent PIN already exists in the app.
   - **Back up the data file** since it becomes the single source of truth.
   - This LAN version replaces the public GitHub Pages demo.

---

## 🔐 Open decisions

3. **Privacy / hosting model.** A GitHub-login allowlist isn't available on a personal plan. Options discussed:
   - *Secret link*: `noindex` + `robots.txt` + unguessable URL + (plan-permitting) private repo. Not searchable; anyone with the link can open it.
   - *Real email allowlist*: move to Cloudflare Pages + Cloudflare Access (free). Becomes moot once the LAN version is live and the public site is taken down.
   - **If the public site stays up at all:** scrub Yiyao's work email from the public git commit history.

4. **Offline PWA layer (optional).** Add a service worker + web app manifest so the hosted version installs to the home screen *and* works with no Wi-Fi (useful for a wall/fridge tablet that may drop signal). Lower priority once the LAN version exists.

---

## 💡 Ideas / maybe (not yet requested)

5. **Left-swipe to mark a quest complete**, as an alternative to tapping. (Right-swipe already skips a quest for the day.)
6. **Confirm star values:** Chess is currently 10 (assumed — wasn't in the effort ranking); "Read for 15 min" (20) ties Piano (20). Decide if Piano should stand alone at the top.

---

## ✅ Already shipped (changelog)

- Initial gamified app: quests, ⭐ stars, levels (Sprout → Mythic), streaks, reward shop, progress tab, confetti + sound.
- Daily auto-reset of quests.
- Chore/reward tuning: daily practices by effort (Duolingo 5; Chinese/Math/Chess 10; Viola 15; Piano 20). Removed "Make the bed."
- Reward costs (easy → hard): Ice cream 40, Pizza 60, Park 80, Movie night 150, Screen time **200**.
- **Viola auto-expires** after 2026-06-30.
- **PIN-locked parent settings** (custom modal, not the browser prompt).
- **"Just for today" ad-hoc tasks** that vanish at the next daily reset.
- **Swipe right to skip** a quest for the day, with tap-to-undo.
- **Robustness:** self-healing data loader + startup guard so a stale/partial copy can't blank the screen.
- **Hosted on GitHub Pages** (temporary demo for showing Bean).
- **Today's date next to the streak** (device system time).
- **Fixed: undo toast was buried under the nav** on mobile and not tappable. Moved to top of screen, allowed wrapping, raised z-index.

---

## 🗒️ Notes / resolved

- *iPad showed a blank board:* root cause was opening the file in the Files app's **Quick Look** preview (not a real browser), compounded by a stale copy. Resolved by hosting at a URL and opening in Safari → Add to Home Screen. The LAN version will make this permanent.

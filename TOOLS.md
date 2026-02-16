# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### Peon-Ping (Local Only)

- Claude Code hooks plugin on user's Mac — NOT an HTTP server
- Install: `curl -fsSL https://raw.githubusercontent.com/PeonPing/peon-ping/main/install.sh | bash -s -- --packs=murloc,peasant_fr,peon_fr,ra2_kirov,rick`
- Plays sounds via `afplay` on macOS, triggered by Claude Code session events
- **Cannot be triggered remotely from this VM** — only works in local Claude Code sessions
- Packs: murloc, peasant_fr, peon_fr, ra2_kirov, rick
- Default packs: peon_fr and peasant_fr (French human voices only)
- Commands: `peon toggle`, `peon status`
- Attempted HTTP relay via cloudflared tunnel (Feb 14) — couldn't get node server running on Mac, abandoned

---

Add whatever helps you do your job. This is your cheat sheet.

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

### Peon-Ping (Sound Relay)

- Relay runs on user's Mac via cloudflared tunnel
- Current URL: `https://parameters-museums-jackson-upper.trycloudflare.com`
- ⚠️ URL changes if cloudflared restarts — ask user for new one
- Play sound: `curl -s -H "X-Volume: 0.8" "<URL>/play?file=packs/<pack>/sounds/<file>"`
- Packs: murloc, peasant_fr, peon_fr, ra2_kirov, rick
- **Default packs: peon_fr and peasant_fr** (French human voices only)
- Use peon_fr for task start/complete/acknowledgements
- Only use murloc/rick/ra2_kirov if user specifically asks

---

Add whatever helps you do your job. This is your cheat sheet.

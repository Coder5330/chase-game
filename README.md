# Chase Game

A top-down survivors-like: dodge and outlast waves of enemies, auto-fire weapons,
level up mid-run, and spend earned resources on permanent upgrades back at the
Homebase.

## Download and play (no Python needed)

Every push builds fresh Windows and Mac executables and publishes them as a new
[GitHub release](../../releases/latest), and also to
[itch.io](https://coder5330.itch.io/chase-game):

- **Windows**: download `chase-game-windows.exe` and double-click it.
- **Mac**: download `chase-game-mac.zip`, unzip it, and double-click
  `chase-game.app`. It isn't signed/notarized, so macOS Gatekeeper will
  refuse to open it the first time — right-click (or Control-click) the app
  and choose **Open**, then confirm in the dialog that appears. You only
  need to do this once.

## Requirements (running from source)

- Python 3
- [pygame](https://www.pygame.org/) (`pip install pygame`)

## Run

```
python3 main.py
```

## Controls

- Arrow keys — move
- Mouse — navigate menus / shop panels
- Enter / Space — continue past the Game Over screen

## Gameplay loop

- **Homebase (hub)**: walk into a trader (Vera / Duncan / Mira) to spend
  resources on permanent meta-upgrades (vitality, combat, mobility). Walk into
  the gold portal to start a run.
- **Run**: survive as long as possible. Enemies spawn and scale with your
  level; killing them drops XP crystals. Leveling up lets you unlock new
  weapons, level up existing ones, or take a stat upgrade. Chests spawn
  periodically — stand near one to channel it open for bonus resources (your
  weapons go offline while channeling).
- Dying ends the run and banks any resources earned back to your save slot.

## Save data

Progress is stored per slot in `saves/slot_<n>.sav` (3 slots, see
`NUM_SAVE_SLOTS` in `settings.py`). Each slot tracks resources, permanent
meta-upgrade levels, highest level reached, and runs played. Saves are
obfuscated and signed so hand-editing the file (or numbers wildly outside
anything a real playthrough could reach) gets rejected back to a fresh save
instead of silently accepted.

## Running tests

```
python3 -m unittest discover -s tests -t . -v
```

No extra dependencies — `tests/` uses the standard library's `unittest` and
runs headless (`SDL_VIDEODRIVER=dummy`), so it doesn't need a real display.
Save tests run against a temp directory and never touch your real `saves/`.

## Project layout

- `main.py` — menu and top-level flow (hub <-> run)
- `game_loop.py` — the `Game` class: run-loop state, update, and draw dispatch
- `hud.py` — in-run HUD/overlay rendering (health, XP bar, pause/countdown/game-over screens)
- `hub.py` — Homebase scene (traders, shop panels, portal)
- `entities/` — `Player`, the `Enemy` base class, and one file per enemy
  archetype (`archer.py`, `spider.py`, `tank.py`, `assassin.py`, `brute.py`,
  `bomber.py`, `shield.py`, `swarm.py`, `elite.py`), registered in
  `registry.py`
- `bullets.py` — weapon/arrow projectile behavior (normal, boomerang,
  homing, pierce, explosive, split, arrow)
- `explosion.py` — particle effect used for `BOMBER` deaths
- `crystals.py` — XP pickups
- `chest.py` — bonus-resource chests
- `elements.py` — reusable UI (Panel, Button)
- `settings.py` — tunable constants, stat tables, and colors
- `save_system.py` — save/load for the 3 save slots (obfuscated + signed)
- `sfx.py` — fail-safe audio (runs fine with zero sound files; picks up
  matching files dropped into `assets/sfx/` automatically)
- `utils.py` — shared helpers (grid drawing, spawning, collisions)
- `tests/` — headless `unittest` regression suite

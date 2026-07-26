# Chase Game

A top-down survivors-like: dodge and outlast waves of enemies, auto-fire weapons,
level up mid-run, and spend earned resources on permanent upgrades back at the
Homebase.

## Requirements

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

Progress is stored per slot in `saves/slot_<n>.json` (3 slots, see
`NUM_SAVE_SLOTS` in `settings.py`). Each slot tracks resources, permanent
meta-upgrade levels, highest level reached, and runs played.

## Project layout

- `main.py` — menu, run loop, and top-level game state
- `hub.py` — Homebase scene (traders, shop panels, portal)
- `entities.py` — Player and Enemy
- `bullets.py` — weapon projectile behavior (normal, boomerang, homing,
  pierce, explosive, split)
- `crystals.py` — XP pickups
- `chest.py` — bonus-resource chests
- `elements.py` — reusable UI (Panel, Button)
- `settings.py` — tunable constants, stat tables, and colors
- `save_system.py` — save/load for the 3 save slots
- `utils.py` — shared helpers (grid drawing, spawning, collisions)

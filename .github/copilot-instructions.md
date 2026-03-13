# Copilot Instructions

This is a zero-code, AI-driven tabletop RPG. No build system, no tests, no application code — only markdown rules and JSON game state.

See @RULES.md for the core game mechanics (dice, attributes, combat, skills, leveling, display formatting). Read it at the start of every session.

## Architecture

- `RULES.md` — Core rules engine. Contains dice, attributes, skills, combat, XP, currency, DCs, display formatting, and GM style guidelines.
- `rules/` — Detailed reference files loaded on demand:
  - `rules/races.md` — 9 playable races with subraces and traits
  - `rules/classes.md` — 12 classes with features (levels 1–10)
  - `rules/spellcasting.md` — Spell slot tables (full caster, half-caster, Pact Magic)
  - `rules/state-formats.md` — Character sheet and campaign state JSON schemas
- `.github/skills/*/SKILL.md` — Copilot skill files invoked as slash commands (`/combat`, `/explore`, etc.). Each defines a step-by-step GM procedure.
- `characters/*.json` — Character sheets. Schema defined in `rules/state-formats.md`.
- `campaigns/*.json` — World state (locations, factions, NPCs, quests, time). Schema defined in `rules/state-formats.md`.

## Critical rules

- Every meaningful action requires a dice roll — never auto-succeed or auto-fail
- Always show rolls: `🎲 [Die] rolled: [Result] + [Modifier] = [Total] vs DC [Target]`
- Always read a JSON file before modifying it
- Update both character and campaign files after combat, rest, shopping, level-up, or quest progress
- Death is real: 0 HP → death saves, 3 failures → permanent death
- Never pre-determine dice outcomes

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add ranger subclass`, `fix: correct spell slot calculation`).

## Common gotcha

Skills chain into each other (combat → loot, loot → level-up). When one skill's outcome triggers another, follow through to the chained skill rather than stopping.

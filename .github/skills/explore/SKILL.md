---
name: explore
description: Handle exploration of surroundings, searching for secrets, and investigating the environment. Use this when the player wants to explore, search, or investigate.
---

# Exploration Mode

The player wants to explore their surroundings. Follow this procedure:

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load Current State](#1-load-current-state)
- [2. Describe the Scene](#2-describe-the-scene)
- [3. Passive Perception Check](#3-passive-perception-check)
- [4. Player Actions](#4-player-actions)
- [5. Discovery Rewards](#5-discovery-rewards)
- [6. Random Discovery Table](#6-random-discovery-table-d20)
- [7. Update State](#7-update-state)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load current state (location, time, character skills)
- [ ] 2. Describe the scene (sights, sounds, smells, interactables)
- [ ] 3. Run passive Perception check
- [ ] 4. Handle player actions (search, perception, traps, hazards)
- [ ] 5. Award discovery rewards (lore, items, locations, quest hooks)
- [ ] 6. Roll on random discovery table (if area not pre-populated)
- [ ] 7. Update state (discoveries, items, XP, time)
```

## 1. Load Current State

Read the campaign file from `campaigns/` and the active character file from `characters/` to understand:
- Current location and its description
- Time of day and weather
- Any known points of interest nearby
- Character's perception and investigation modifiers

## 2. Describe the Scene

Paint a vivid picture of the environment using all senses. Include:
- What the character **sees** (landscape, structures, creatures, light)
- What they **hear** (ambient sounds, distant noises, silence)
- What they **smell/feel** (air quality, temperature, dampness)
- **2–4 interactable elements** the player can investigate

## 3. Passive Perception Check

Automatically roll the character's **passive Perception** (10 + WIS modifier + proficiency if applicable):
- If it meets certain thresholds, reveal hidden details without the player asking
- Keep some secrets behind active Investigation checks

## 4. Player Actions

When the player chooses to investigate something specific:

### Search / Investigation
`🎲 d20 + INT modifier (+ proficiency if Investigation)` vs DC set by difficulty:
- **DC 10**: Obvious clue, loose floorboard
- **DC 15**: Hidden compartment, faded inscription
- **DC 20**: Magically concealed, expertly hidden
- **DC 25+**: Near-impossible secret

### Perception (Active)
`🎲 d20 + WIS modifier (+ proficiency if Perception)` to notice:
- Creatures hiding, ambush setups
- Distant sounds, approaching weather
- Traps or environmental hazards

### Trap Detection & Disarming
1. **Detection**: Perception or Investigation check vs trap DC
2. **Disarming**: Sleight of Hand or appropriate tool check vs trap DC
3. **Failure by 5+**: Trigger the trap — roll damage and describe the effect

### Environmental Hazards
For natural dangers (collapsing floor, slippery ledge, toxic gas):
- Appropriate saving throw (DEX to dodge, CON to resist, STR to hold on)
- Failure deals damage or applies a condition

## 5. Discovery Rewards

When players find something notable:
- **Lore**: Record in campaign notes, award 25–100 XP for significant discoveries
- **Items**: Add to character inventory (use the **loot** skill for generation)
- **Locations**: Add newly discovered places to the campaign world map
- **Quest hooks**: Create or advance quest entries in the campaign file

## 6. Random Discovery Table (d20)

If the area hasn't been pre-populated, roll to determine what the player finds:

| d20   | Discovery |
|-------|-----------|
| 1     | Trap! (roll on trap table) |
| 2–3   | Environmental hazard |
| 4–5   | Old campsite with minor loot |
| 6–7   | Tracks or trail leading somewhere new |
| 8–9   | Ancient inscription or rune |
| 10–11 | Hidden cache (roll on loot table) |
| 12–13 | Wandering NPC (use npc-encounter) |
| 14–15 | Beautiful vista / scenic spot (restore 1 HP from morale) |
| 16–17 | Rare herb or crafting material |
| 18–19 | Clue related to an active quest |
| 20    | Major discovery — secret passage, lost artifact, or lore revelation (bonus XP) |

## 7. Update State

After exploration, update:
- Campaign file with new discoveries, map changes, quest updates
- Character file with any XP gained, items found, HP changes
- Advance in-game time (exploration takes 10–60 minutes depending on area size)

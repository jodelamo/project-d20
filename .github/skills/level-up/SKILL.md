---
name: level-up
description: Handle character advancement when XP reaches the level-up threshold. Use this when a character levels up or the player asks to level up.
---

# Level Up

Handle character advancement when XP reaches the threshold.

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load Character](#1-load-character)
- [2. Announce the Level Up](#2-announce-the-level-up)
- [3. Apply Core Improvements](#3-apply-core-improvements)
- [4. Skill Proficiencies](#4-skill-proficiencies)
- [5. Class Features by Level](#5-class-features-by-level)
- [6. Ability Score Improvements](#6-ability-score-improvements-levels-4-8-etc)
- [7. New Spells](#7-new-spells-casters)
- [8. Update XP Threshold](#8-update-xp-threshold)
- [9. Present the Updated Character](#9-present-the-updated-character)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load character and verify XP threshold
- [ ] 2. Announce the level up
- [ ] 3. Roll HP increase and update proficiency bonus
- [ ] 4. Apply new skill proficiencies/expertise (if applicable)
- [ ] 5. Apply class features from class-features.md
- [ ] 6. Handle ASI or feat selection (levels 4, 8)
- [ ] 7. Select new spells (if caster)
- [ ] 8. Set new XP threshold
- [ ] 9. Present updated character sheet and save
```

## 1. Load Character

Read the character file. Verify:
- Current XP ≥ XP threshold for next level
- Current level and class
- All current stats for reference

If XP is insufficient: *"You need [X] more XP to reach level [N]. Keep adventuring!"*

## 2. Announce the Level Up

Narrate the level-up dramatically:
*"Experience courses through you like fire. Battles fought, lessons learned, secrets uncovered — it all crystallizes into newfound power. You are now **Level [N]**!"*

## 3. Apply Core Improvements

### Hit Points
Roll the class hit die (or take the average, player's choice). Look up the hit die in `rules/classes.md`:
- d12: Barbarian | d10: Fighter, Paladin, Ranger | d8: Bard, Cleric, Druid, Monk, Rogue, Warlock | d6: Sorcerer, Wizard

Show the roll: `🎲 HP roll: [result] + CON mod [mod] = +[total] HP → New max HP: [new_max]`

Minimum HP gain per level: 1 (even with negative CON modifier).

### Proficiency Bonus
Update if crossing a threshold:
| Levels | Bonus |
|--------|-------|
| 1–4    | +2    |
| 5–8    | +3    |
| 9–10   | +4    |

### Hit Dice
Gain 1 additional hit die of the class type.

## 4. Skill Proficiencies

At certain levels, some classes gain new skill proficiencies or expertise:
- **Rogue**: Additional Expertise at level 6 (double proficiency on 2 more skills)
- **Bard**: Additional Expertise at level 10 (double proficiency on 2 more skills)
- **Bard (Lore)**: 3 additional skill proficiencies at level 3

No other class gains new skill proficiencies on level-up (proficiencies are fixed at character creation).

## 5. Class Features by Level

Look up the character's class in `class-features.md` for the full feature table (levels 1–10). Apply all features gained at the new level.

## 6. Ability Score Improvements (Levels 4, 8, etc.)

When an ASI is earned, the player chooses:
- **+2 to one attribute** (max 20)
- **+1 to two attributes** (max 20 each)
- **A Feat** (special ability in place of stat increase)

See `feats.md` for the full feat list.

## 7. New Spells (Casters)

If the character is a spellcaster, they gain new spells at the new level:
- **Wizard**: +2 spells added to spellbook (any level they can cast)
- **Cleric/Druid**: Access to full class spell list up to new max spell level (prepare WIS mod + level)
- **Bard/Sorcerer**: +1 spell known (can swap 1 old spell for a new one)
- **Ranger**: +1 spell known at levels when new slots appear
- **Warlock**: +1 spell known (can swap 1 old spell), Pact Magic slots upgrade
- **Paladin**: Access to full paladin spell list up to new max spell level (prepare CHA mod + half level)

Present appropriate spell options and let the player choose.

## 8. Update XP Threshold

Set the new XP target for the next level per the XP table in RULES.md.

## 9. Present the Updated Character

Display the full updated character sheet showing all changes highlighted. Save the updated character file.

End with: *"You feel stronger, sharper, more capable. The road ahead holds new challenges worthy of your growing power."*

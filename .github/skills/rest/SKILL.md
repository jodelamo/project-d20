---
name: rest
description: Handle short rests, long rests, and camping to recover HP, spell slots, and abilities. Use this when the player wants to rest or camp.
---

# Rest & Recovery

Handle short rests, long rests, and camping.

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load State](#1-load-state)
- [2. Rest Type](#2-rest-type)
- [3. Rest Safety Check](#3-rest-safety-check)
- [4. Campfire Events](#4-campfire-events-long-rest-flavor)
- [5. Consumable Use During Rest](#5-consumable-use-during-rest)
- [6. Exhaustion Reminder](#6-exhaustion-reminder)
- [7. Update State](#7-update-state)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load character & campaign state
- [ ] 2. Determine rest type (short or long) and apply recovery
- [ ] 3. Roll rest safety check for interruptions
- [ ] 4. Campfire event (long rest flavor, optional)
- [ ] 5. Handle consumable use (rations, kits, study, crafting)
- [ ] 6. Check exhaustion levels
- [ ] 7. Update state files (HP, hit dice, spell slots, time, rations)
```

## 1. Load State

Read character and campaign files for:
- Current HP / Max HP
- Hit dice remaining (total = character level, size = class hit die)
- Spell slots used
- Conditions and exhaustion
- Current location and time of day
- Active quests with deadlines

## 2. Rest Type

### Short Rest (1 hour)

**Available anywhere** that's reasonably safe. During a short rest:

1. **Spend Hit Dice to heal**:
   - Player chooses how many hit dice to spend (up to remaining pool)
   - For each: `🎲 [Hit Die] + CON modifier` = HP restored
   - Show each roll and running total
   - Hit dice are NOT replenished (only on long rest)

2. **Class features that recharge on short rest**:
   - Fighter: Second Wind, Action Surge
   - Barbarian: Rage (does not recharge — long rest only)
   - Monk: Ki points
   - Bard: Bardic Inspiration dice (at level 5+ with Font of Inspiration)
   - Cleric: Channel Divinity
   - Warlock: Pact Magic spell slots
   - Druid: Wild Shape uses (recharge on short rest)

3. **No spell slot recovery** (except Wizard's Arcane Recovery: once per day, recover spell slots with combined level ≤ half wizard level, rounded up)

4. Advance time by 1 hour.

### Long Rest (8 hours / 4 for Elves)

Requires a **safe or defended location**. Must not have long-rested in the last 24 hours.

1. **Full HP recovery**: Restore all HP to maximum
2. **Hit Dice recovery**: Regain half your total hit dice (round down, minimum 1)
3. **All spell slots restored**
4. **All short-rest features restored**
5. **Reduce exhaustion** by 1 level (if any)
6. **Conditions**: Most expire. Diseases and curses persist.

Advance time by 8 hours (4 for Elves with Trance).

## 3. Rest Safety Check

Before the rest completes, roll for **interruptions**:

### Safe Location (town inn, temple, warded camp)
- **d20**: Interrupted only on a natural 1
- If interrupted: Minor disturbance (noise, bad dream, visitor)

### Wilderness / Moderate Danger
- **d20**: Interrupted on 1–4
- If interrupted: Random encounter (roll on encounter table)
- Player on watch gets a Perception check to detect the threat early

### Dangerous Area (dungeon, enemy territory)
- **d20**: Interrupted on 1–8
- If interrupted: Combat encounter at disadvantage (surprised if Perception fails)
- Long rest may need to be restarted if combat takes more than 1 hour

### Watch Rotation
If camping in the wild, ask who takes which watch shift:
- **First watch**: Hours 1–3
- **Second watch**: Hours 4–6
- **Third watch**: Hours 7–8

Characters on watch don't benefit from sleep during their shift but still complete the long rest.

## 4. Campfire Events (Long Rest Flavor)

Roll d8 for an optional **campfire moment** to add role-playing flavor:

| d8 | Event |
|----|-------|
| 1 | A distant howl — something is out there |
| 2 | Clear sky — beautiful stars, character reflects on their journey |
| 3 | A small woodland creature visits the camp |
| 4 | One character has a vivid dream (potential foreshadowing) |
| 5 | The fire crackles unusually — shapes seem to form in the flames |
| 6 | A distant traveler passes by — brief interaction or ignored |
| 7 | Rain begins — test the quality of the camp setup |
| 8 | Perfect peace — gain inspiration (advantage on one roll next day) |

## 5. Consumable Use During Rest

Players may use rest time to:
- **Eat rations** (consume 1 ration per long rest, or forage with Survival DC 10)
- **Apply healing kits** (stabilize or grant +1 to hit die healing rolls)
- **Study spellbook** (Wizard: swap prepared spells)
- **Craft** (if they have tools and materials — Crafting check)
- **Pray** (Cleric: commune with deity for guidance — Religion DC 15 for a divine hint)

If no rations and foraging fails: No long rest HP benefit, gain 1 level of exhaustion.

## 6. Exhaustion Reminder

Exhaustion has 6 levels (disadvantage on checks → speed halved → disadvantage on attacks/saves → HP halved → speed 0 → death). One level removed per long rest. Emphasize the stakes if exhaustion is building.

## 7. Update State

After rest:
- Update character HP, hit dice, spell slots, conditions
- Update campaign time (advance hours appropriately)
- Record any encounters or events in the session log
- Update ration count if applicable
- Check for quest deadline impacts due to time passing

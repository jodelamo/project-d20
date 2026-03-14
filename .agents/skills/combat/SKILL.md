---
name: combat
description: Handle tactical combat encounters with initiative, attacks, saving throws, and dice rolls. Use this when the player wants to fight enemies or resolve combat.
---

# Combat Encounter

Handle tactical combat following these rules precisely. **Every attack, save, and effect requires a dice roll.**

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load State](#1-load-state)
- [2. Encounter Generation](#2-encounter-generation-if-new-combat)
- [3. Initiative](#3-initiative)
- [4. Combat Rounds](#4-combat-rounds)
- [5. Conditions in Combat](#5-conditions-in-combat)
- [6. Death & Dying](#6-death--dying)
- [7. End of Combat](#7-end-of-combat)
- [8. Update State](#8-update-state)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load party & campaign state
- [ ] 2. Generate encounter (if new combat)
- [ ] 3. Roll initiative for all combatants (all party members + all enemies)
- [ ] 4. Run combat rounds (party turns → enemy turns, repeat)
- [ ] 5. Track conditions each turn
- [ ] 6. Handle death & dying (if any creature hits 0 HP)
- [ ] 7. End combat (tally XP, loot, healing check, narrative)
- [ ] 8. Update state files (HP, XP, items, spell slots, level-up check for each party member)
```

## 1. Load State

Read the active party and campaign files. Determine:
- Each party member's combat stats (HP, AC, attack bonuses, weapons, spells)
- Current enemies (or generate new ones — see encounter generation below)
- Environment and terrain features

## 2. Encounter Generation (if new combat)

If no enemies exist yet, generate an encounter scaled to party level:

### Monster Challenge Rating
Roll d100 for encounter difficulty:
- **01–40**: Easy (CR = party level − 2, minimum ½)
- **41–70**: Medium (CR = party level − 1)
- **71–90**: Hard (CR = party level)
- **91–100**: Deadly (CR = party level + 1 or +2)

### Generate Enemies
For each enemy, create:
- Name, race/type, brief description
- Alignment (for intelligent creatures — influences whether they surrender, negotiate, or fight to the death)
- HP (roll hit dice), AC, attack bonus, damage
- 1–2 special abilities appropriate to the creature type
- XP reward based on CR

Present enemies using the display formats from `RULES.md` § "Display Formatting — Monster Cards":
- **1 enemy**: Show a **monster card** with stats and a short description
- **2+ enemies**: Show a **monster roster** with compact per-enemy stats
- **Boss + minions**: Monster card for the boss, then a roster for the minions

## 3. Initiative

All combatants roll initiative: `🎲 d20 + DEX modifier`

Display the initiative order as a clear list (all party members and all enemies):
```
⚔️ Initiative Order:
1. Goblin Archer — 18
2. Kaelith (Fighter) — 15
3. Seraphine (Wizard) — 14
4. Goblin Warrior — 12
5. Thorne (Cleric) — 10
6. Goblin Shaman — 8
```

## 4. Combat Rounds

Each round, cycle through the initiative order. For each turn:

### Party Member Turns
On each party member's turn, present the tactical situation and choose their action (see the **start** skill's "Autonomous Character Decisions" for how to decide during auto-play, or ask the player during manual play):
- **Attack** (melee or ranged)
- **Cast a spell** (if caster)
- **Use an item** (potion, scroll, etc.)
- **Dash** (double movement)
- **Dodge** (attacks against you have disadvantage)
- **Disengage** (move without provoking opportunity attacks)
- **Hide** (Stealth check)
- **Help** (give an ally advantage)
- **Other** (improvised actions — set a DC and let them try!)

#### Attack Resolution
1. `🎲 d20 + ATK modifier` vs target's AC
2. **Hit**: Roll damage die + modifier. Describe the hit vividly.
3. **Miss**: Describe the near-miss.
4. **Natural 20**: CRITICAL HIT — use the `★ NATURAL 20 ★` format (see `RULES.md` § "Display Formatting — Critical Hits & Misses"). Double all damage dice, describe epicly.
5. **Natural 1**: Critical miss — use the `✖ NATURAL 1 ✖` format. Describe the fumble (no extra penalty, just flavor).

### Enemy Turns
The GM controls all enemies. For each:
1. Describe their action narratively
2. Roll attack: `🎲 d20 + enemy ATK` vs target party member's AC
3. On hit, roll damage and update that character's HP
4. Use enemy special abilities when tactically appropriate (not just to punish)
5. Enemies should use basic targeting logic — attack the closest threat, focus on low-AC targets, or prioritize healers

### Saving Throws
When a spell or effect requires a save:
`🎲 d20 + attribute modifier (+ proficiency if proficient in that save)`
- **Meet or exceed the DC**: Success (half damage or no effect)
- **Fail**: Full effect

## 5. Conditions in Combat

Track and enforce conditions per RULES.md. At the start of each affected creature's turn, announce active conditions and apply their effects before the creature acts.

## 6. Death & Dying

When a character drops to 0 HP:
1. They fall **unconscious**
2. Each turn, roll a **death saving throw**: `🎲 d20`
   - 10+: Success
   - <10: Failure
   - Natural 20: Regain 1 HP and consciousness!
   - Natural 1: Counts as 2 failures
3. **3 successes**: Stabilized (unconscious but alive)
4. **3 failures**: **DEATH** — narrate solemnly

Any damage while at 0 HP = automatic death save failure. A critical hit against a creature at 0 HP counts as 2 death save failures. Massive damage (remaining damage ≥ max HP) = instant death.

## 7. End of Combat

When all enemies are defeated or combat ends:

1. **Tally XP**: Sum enemy XP values, divide equally among surviving party members
2. **Loot**: Roll for enemy drops (use the **loot** skill or quick table below)
3. **Healing check**: Show every party member's current HP and note available healing options
4. **Narrative**: Describe the aftermath — the silence after battle, the scene

### Quick Loot (d6 per enemy)
Use item icons per RULES.md § "Display Formatting — Icons & Items":
| d6  | Drop |
|-----|------|
| 1–2 | Nothing |
| 3–4 | 🪙 d6 gold coins |
| 5   | 🧪 Minor consumable (potion, scroll 📜) |
| 6   | ⚔️ Weapon, 🛡️ armor, or 🗝️ notable item |

## 8. Update State

After combat:
- Update **every** party member's HP, spell slots used, items consumed
- Add XP to each character file. **Check if any member reached the level-up threshold!**
- Update campaign file with combat results, enemy status
- If a character leveled up, prompt the player to use the **level-up** skill

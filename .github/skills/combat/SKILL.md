---
name: combat
description: Handle tactical combat encounters with initiative, attacks, saving throws, and dice rolls. Use this when the player wants to fight enemies or resolve combat.
---

# Combat Encounter

Handle tactical combat following these rules precisely. **Every attack, save, and effect requires a dice roll.**

## 1. Load State

Read the active character and campaign files. Determine:
- Character's combat stats (HP, AC, attack bonuses, weapons, spells)
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
- HP (roll hit dice), AC, attack bonus, damage
- 1–2 special abilities appropriate to the creature type
- XP reward based on CR

Present enemies dramatically: *"From the shadows emerge..."*

## 3. Initiative

All combatants roll initiative: `🎲 d20 + DEX modifier`

Display the initiative order as a clear list:
```
⚔️ Initiative Order:
1. Goblin Archer — 18
2. [Player Character] — 15
3. Goblin Warrior — 12
4. Goblin Shaman — 8
```

## 4. Combat Rounds

Each round, cycle through the initiative order. For each turn:

### Player's Turn
Present the tactical situation and offer options:
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
4. **Natural 20**: CRITICAL HIT — double all damage dice, describe epicly.
5. **Natural 1**: Critical miss — describe the fumble (no extra penalty, just flavor).

### Enemy Turns
The GM controls all enemies. For each:
1. Describe their action narratively
2. Roll attack: `🎲 d20 + enemy ATK` vs player's AC
3. On hit, roll damage and update player HP
4. Use enemy special abilities when tactically appropriate (not just to punish)

### Saving Throws
When a spell or effect requires a save:
`🎲 d20 + attribute modifier (+ proficiency if proficient in that save)`
- **Meet or exceed the DC**: Success (half damage or no effect)
- **Fail**: Full effect

## 5. Conditions in Combat

Track and enforce conditions. At the start of each affected creature's turn, note active conditions:
- **Poisoned**: Disadvantage on attacks and ability checks
- **Stunned**: Can't move or act, auto-fail STR/DEX saves, attacks have advantage
- **Prone**: Disadvantage on attacks, melee attacks against have advantage, ranged have disadvantage
- **Frightened**: Disadvantage on checks/attacks while source is in sight, can't willingly move closer

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

Any damage while at 0 HP = automatic death save failure. Massive damage (remaining damage ≥ max HP) = instant death.

## 7. End of Combat

When all enemies are defeated or combat ends:

1. **Tally XP**: Sum enemy XP values, divide among party members
2. **Loot**: Roll for enemy drops (use loot prompt or quick table below)
3. **Healing check**: Remind player of current HP and available healing
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
- Update character HP, spell slots used, items consumed
- Add XP to character file. **Check if level-up threshold is reached!**
- Update campaign file with combat results, enemy status
- If a character leveled up, prompt the player to use the **level-up** prompt

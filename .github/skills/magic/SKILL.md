---
name: magic
description: Handle spellcasting, ritual magic, magical item use, and wild magic events. Use this when the player wants to cast a spell or use magic.
---

# Magic & Spellcasting

Handle all magical actions — spellcasting, ritual magic, magical item use, and wild magic events.

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load Caster State](#1-load-caster-state)
- [2. Spell Selection](#2-spell-selection)
- [3. Spell Slot Check](#3-spell-slot-check)
- [4. Resolve the Spell](#4-resolve-the-spell)
- [5. Cantrip Scaling](#5-cantrip-scaling)
- [6. Spell Compendium](#6-spell-compendium)
- [7. Wild Magic](#7-wild-magic-sorcerer--optional)
- [8. Update State](#8-update-state)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load caster state (class, ability, spells, slots, concentration)
- [ ] 2. Identify or suggest the spell
- [ ] 3. Check spell slot availability (cantrip / slot / upcast)
- [ ] 4. Resolve the spell (attack roll, saving throw, healing, AoE, concentration)
- [ ] 5. Apply cantrip scaling (if cantrip)
- [ ] 6. Reference spells.md for spell details
- [ ] 7. Roll wild magic surge (if Wild Magic Sorcerer)
- [ ] 8. Update state (slots, HP, concentration, conditions, XP)
```

## 1. Load Caster State

Read the character file to determine:
- Spellcasting class and ability (INT for Wizard, WIS for Cleric/Ranger/Druid, CHA for Bard/Sorcerer/Warlock/Paladin)
- Known/prepared spells and cantrips
- Available spell slots by level
- Spell attack bonus: `proficiency + spellcasting modifier`
- Spell save DC: `8 + proficiency + spellcasting modifier`
- Any active concentration spells

## 2. Spell Selection

If the player names a specific spell, use it. If they describe an effect, suggest the closest matching spell from their known/prepared list.

If the player wants to cast a spell they don't know: **"You don't have that spell prepared/known. Here's what you can cast..."** and list options.

## 3. Spell Slot Check

- **Cantrips**: Always available, no slot needed
- **Leveled spells**: Require and consume a spell slot of the spell's level or higher
- If no slots remain: *"You've exhausted your magical reserves. You need to rest to recover spell slots."*
- **Upcasting**: If cast at a higher slot level, apply enhanced effects (extra damage die, additional targets, etc.)

## 4. Resolve the Spell

### Spell Attack Rolls
For spells requiring an attack roll:
```
🎲 d20 + spell attack bonus vs target AC
→ Hit: Roll damage
→ Miss: Spell fizzles against the target
→ Nat 20: Critical — double damage dice!
```

### Saving Throw Spells
For spells requiring the target to save:
```
Target must make a [Attribute] saving throw:
🎲 d20 + target's [Attribute] modifier = [total] vs your Spell DC [dc]
→ Fail: Full effect
→ Save: Half damage / reduced effect / no effect (spell-dependent)
```

### Healing Spells
Roll the specified healing dice:
```
🎲 [dice] + spellcasting modifier = [total] HP restored
[Character] HP: [old] → [new] / [max]
```

### Area of Effect
For AoE spells, each creature in the area makes a saving throw individually. Roll for each and narrate the results.

### Concentration
If the spell requires **concentration**:
- Note it as active on the character
- If the caster takes damage, they must make a **Constitution saving throw**:
  - DC = 10 or half the damage taken, whichever is higher
  - Failure: Spell ends immediately
- Only one concentration spell at a time — casting another ends the first

## 5. Cantrip Scaling

Cantrip damage scales with **character level** (not class level):

| Character Level | Cantrip Dice |
|----------------|-------------|
| 1–4            | 1 die       |
| 5–10           | 2 dice      |
| 11–16          | 3 dice      |
| 17+            | 4 dice      |

## 6. Spell Compendium

Refer to `spells.md` for the full spell compendium (cantrips through 3rd level). Generate additional spells as needed, following the power curve and slot-level guidelines.

## 7. Wild Magic (Sorcerer — Optional)

When a Wild Magic Sorcerer rolls a natural 1 on a spell attack or a natural 20, roll on the surge table in `wild-magic.md`.

## 8. Update State

After spellcasting:
- Deduct the spell slot used from the character file
- Update HP if healing or damage occurred
- Note active concentration spells
- Record any conditions applied to enemies/allies
- Award XP for creative spell use (25–50 XP)

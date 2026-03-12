---
name: level-up
description: Handle character advancement when XP reaches the level-up threshold. Use this when a character levels up or the player asks to level up.
---

# Level Up

Handle character advancement when XP reaches the threshold.

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
Roll the class hit die (or take the average, player's choice):
- **Barbarian**: `🎲 d12 + CON modifier` (average: 7 + CON)
- **Fighter**: `🎲 d10 + CON modifier` (average: 6 + CON)
- **Paladin**: `🎲 d10 + CON modifier` (average: 6 + CON)
- **Ranger**: `🎲 d10 + CON modifier` (average: 6 + CON)
- **Bard**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Cleric**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Druid**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Monk**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Rogue**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Warlock**: `🎲 d8 + CON modifier` (average: 5 + CON)
- **Sorcerer**: `🎲 d6 + CON modifier` (average: 4 + CON)
- **Wizard**: `🎲 d6 + CON modifier` (average: 4 + CON)

Show the roll: `🎲 HP roll: [result] + CON mod [mod] = +[total] HP → New max HP: [new_max]`

Minimum HP gain per level: 1 (even with negative CON modifier).

### Proficiency Bonus
Update if crossing a threshold:
| Levels | Bonus |
|--------|-------|
| 1–4    | +2    |
| 5–8    | +3    |
| 9–12   | +4    |
| 13–16  | +5    |
| 17–20  | +6    |

### Hit Dice
Gain 1 additional hit die of the class type.

## 4. Skill Proficiencies

At certain levels, some classes gain new skill proficiencies or expertise:
- **Rogue**: Additional Expertise at level 6 (double proficiency on 2 more skills)
- **Bard**: Additional Expertise at level 10 (double proficiency on 2 more skills)
- **Bard (Lore)**: 3 additional skill proficiencies at level 3

No other class gains new skill proficiencies on level-up (proficiencies are fixed at character creation).

## 5. Class Features by Level

### Barbarian
| Level | Feature |
|-------|---------|
| 1 | Rage (2/long rest, +2 damage), Unarmored Defense (AC = 10 + DEX + CON) |
| 2 | Reckless Attack (advantage on STR attacks, attacks against you have advantage), Danger Sense (advantage on DEX saves you can see) |
| 3 | Primal Path (Berserker: Frenzy — bonus action attack while raging, Path of the Totem Warrior: totem spirits) |
| 4 | Ability Score Improvement |
| 5 | Extra Attack, Fast Movement (+10 speed while unarmored) |
| 6 | Path Feature |
| 7 | Feral Instinct (advantage on initiative, can act while surprised if raging) |
| 8 | Ability Score Improvement |
| 9 | Brutal Critical (+1 extra damage die on crit) |
| 10 | Path Feature |

### Fighter
| Level | Feature |
|-------|---------|
| 1 | Fighting Style (choose: Defense +1AC, Dueling +2 damage, Great Weapon reroll 1s/2s, Archery +2 ranged, Protection, Two-Weapon Fighting), Second Wind (1d10 + level HP, 1/short rest) |
| 2 | Action Surge (1 extra action, 1/short rest) |
| 3 | Martial Archetype (Champion: crit on 19–20, Battle Master: maneuvers, Eldritch Knight: spellcasting) |
| 4 | Ability Score Improvement |
| 5 | Extra Attack (2 attacks per Attack action) |
| 6 | Ability Score Improvement |
| 7 | Archetype Feature |
| 8 | Ability Score Improvement |
| 9 | Indomitable (reroll a failed save, 1/long rest) |
| 10 | Archetype Feature |

### Rogue
| Level | Feature |
|-------|---------|
| 1 | Sneak Attack +1d6, Expertise (double proficiency on 2 skills) |
| 2 | Cunning Action (Dash, Disengage, or Hide as bonus action) |
| 3 | Roguish Archetype (Thief: fast hands/climb speed, Assassin: auto-crit surprised foes, Arcane Trickster: spellcasting) |
| 4 | Ability Score Improvement |
| 5 | Uncanny Dodge (halve one attack's damage, reaction) |
| 6 | Expertise (2 more skills) |
| 7 | Evasion (DEX save AoE: success=0, fail=half) |
| 8 | Ability Score Improvement |
| 9 | Sneak Attack +5d6 (cumulative: +1d6 every odd level) |
| 10 | Ability Score Improvement |

### Wizard
| Level | Feature |
|-------|---------|
| 1 | Arcane Recovery (recover slots = half level rounded up on short rest, 1/day), Spellcasting |
| 2 | Arcane Tradition (Evocation: Sculpt Spells, Abjuration: Arcane Ward, Divination: Portent) |
| 3 | 2nd-level spell slots |
| 4 | Ability Score Improvement |
| 5 | 3rd-level spell slots |
| 6 | Tradition Feature |
| 7 | 4th-level spell slots |
| 8 | Ability Score Improvement |
| 9 | 5th-level spell slots |
| 10 | Tradition Feature |

### Sorcerer
| Level | Feature |
|-------|---------|
| 1 | Sorcerous Origin (Draconic Bloodline: +1 HP/level + AC 13 unarmored, Wild Magic: Wild Magic Surge + Tides of Chaos), Spellcasting |
| 2 | Font of Magic (sorcery points = level, convert between spell slots and points) |
| 3 | Metamagic (choose 2: Twinned, Quickened, Subtle, Empowered, etc.), 2nd-level spell slots |
| 4 | Ability Score Improvement |
| 5 | 3rd-level spell slots |
| 6 | Origin Feature |
| 7 | 4th-level spell slots |
| 8 | Ability Score Improvement |
| 9 | 5th-level spell slots |
| 10 | Metamagic (learn 1 more) |

### Warlock
| Level | Feature |
|-------|---------|
| 1 | Otherworldly Patron (Archfey: charm, Fiend: temp HP on kill, Great Old One: telepathy), Pact Magic (1 slot, recharges on short rest) |
| 2 | Eldritch Invocations (choose 2 — e.g., Agonizing Blast, Devil's Sight, Mask of Many Faces) |
| 3 | Pact Boon (Pact of the Chain: familiar, Pact of the Blade: weapon, Pact of the Tome: cantrips), 2nd-level slots |
| 4 | Ability Score Improvement |
| 5 | 3rd-level slots, Invocation (learn 1 more) |
| 6 | Patron Feature |
| 7 | 4th-level slots, Invocation (learn 1 more) |
| 8 | Ability Score Improvement |
| 9 | 5th-level slots, Invocation (learn 1 more) |
| 10 | Patron Feature |

### Druid
| Level | Feature |
|-------|---------|
| 1 | Druidic (secret language), Spellcasting |
| 2 | Wild Shape (CR ¼, 2 uses/short rest), Druid Circle (Circle of the Land: bonus cantrip + natural recovery, Circle of the Moon: CR 1 Wild Shape + combat form) |
| 3 | 2nd-level spell slots |
| 4 | Ability Score Improvement, Wild Shape CR ½ |
| 5 | 3rd-level spell slots |
| 6 | Circle Feature |
| 7 | 4th-level spell slots |
| 8 | Ability Score Improvement, Wild Shape CR 1 |
| 9 | 5th-level spell slots |
| 10 | Circle Feature |

### Monk
| Level | Feature |
|-------|---------|
| 1 | Unarmored Defense (AC = 10 + DEX + WIS), Martial Arts (use DEX for unarmed/monk weapons, bonus unarmed strike, 1d4 damage die) |
| 2 | Ki (points = level — Flurry of Blows, Patient Defense, Step of the Wind), Unarmored Movement (+10 speed) |
| 3 | Monastic Tradition (Open Hand: stunning strike features, Shadow: shadow arts, Four Elements: elemental disciplines), Deflect Missiles |
| 4 | Ability Score Improvement, Slow Fall (reduce falling damage by 5× level) |
| 5 | Extra Attack, Stunning Strike (1 ki — CON save or stunned), Martial Arts d6 |
| 6 | Ki-Empowered Strikes (unarmed = magical), Tradition Feature, Unarmored Movement (+15) |
| 7 | Evasion, Stillness of Mind |
| 8 | Ability Score Improvement |
| 9 | Unarmored Movement Improvement (run on vertical surfaces and water) |
| 10 | Purity of Body (immune to disease and poison) |

### Paladin
| Level | Feature |
|-------|---------|
| 1 | Divine Sense (detect celestials/fiends/undead), Lay on Hands (HP pool = 5 × level) |
| 2 | Fighting Style (Defense, Dueling, Great Weapon, Protection), Spellcasting, Divine Smite (2d8 radiant on hit, +1d8/slot above 1st, +1d8 vs undead/fiend) |
| 3 | Sacred Oath (Oath of Devotion: Sacred Weapon + Turn the Unholy, Oath of the Ancients: nature powers, Oath of Vengeance: hunting powers), Channel Divinity |
| 4 | Ability Score Improvement |
| 5 | Extra Attack, 2nd-level spell slots |
| 6 | Aura of Protection (+CHA mod to saves for allies within 10 ft) |
| 7 | Oath Feature |
| 8 | Ability Score Improvement |
| 9 | 3rd-level spell slots |
| 10 | Aura of Courage (you and allies within 10 ft can't be frightened) |

### Cleric
| Level | Feature |
|-------|---------|
| 1 | Divine Domain (Life: bonus healing, Light: fire powers, War: bonus attacks) |
| 2 | Channel Divinity (Turn Undead + domain power, 1/short rest) |
| 3 | 2nd-level spell slots |
| 4 | Ability Score Improvement |
| 5 | Destroy Undead (CR ½), 3rd-level slots |
| 6 | Channel Divinity (2/short rest), Domain Feature |
| 7 | 4th-level spell slots |
| 8 | Ability Score Improvement, Domain Feature |
| 9 | 5th-level spell slots |
| 10 | Divine Intervention (roll d100 ≤ level for divine help) |

### Ranger
| Level | Feature |
|-------|---------|
| 1 | Favored Enemy (+2 to track/recall info), Natural Explorer (ignore difficult terrain in favored land) |
| 2 | Fighting Style + Spellcasting (2 first-level slots, 2 spells known) |
| 3 | Ranger Archetype (Hunter: combat bonuses, Beast Master: animal companion) |
| 4 | Ability Score Improvement |
| 5 | Extra Attack, 2nd-level spell slots |
| 6 | Favored Enemy improvement (+1 type), Natural Explorer (+1 terrain) |
| 7 | Archetype Feature |
| 8 | Ability Score Improvement, Land's Stride |
| 9 | 3rd-level spell slots |
| 10 | Hide in Plain Sight (+10 Stealth in natural terrain) |

### Bard
| Level | Feature |
|-------|---------|
| 1 | Bardic Inspiration d6 (CHA mod uses/long rest), Spellcasting |
| 2 | Jack of All Trades (+half proficiency to non-proficient checks), Song of Rest (d6 bonus healing on short rest) |
| 3 | Bard College (Lore: extra skills + Cutting Words, Valor: martial + Combat Inspiration), Expertise (2 skills) |
| 4 | Ability Score Improvement |
| 5 | Bardic Inspiration d8, Font of Inspiration (recharge on short rest) |
| 6 | College Feature, Countercharm |
| 7 | 4th-level spell slots |
| 8 | Ability Score Improvement |
| 9 | Song of Rest d8, 5th-level spell slots |
| 10 | Bardic Inspiration d10, Expertise (2 more skills), Magical Secrets (learn 2 spells from any class) |

## 6. Ability Score Improvements (Levels 4, 8, etc.)

When an ASI is earned, the player chooses:
- **+2 to one attribute** (max 20)
- **+1 to two attributes** (max 20 each)
- **A Feat** (special ability in place of stat increase)

### Sample Feats
| Feat | Effect |
|------|--------|
| Alert | +5 initiative, can't be surprised |
| Tough | +2 HP per level (retroactive) |
| Lucky | 3 luck points/long rest — reroll any d20 |
| Sharpshooter | −5 attack for +10 ranged damage, ignore cover |
| Great Weapon Master | −5 attack for +10 melee damage (two-handed), bonus attack on crit/kill |
| War Caster | Advantage on concentration saves, somatic with hands full |
| Resilient | +1 to chosen attribute, gain save proficiency in it |
| Mobile | +10 speed, no opportunity attacks from creatures you attack |

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

Set the new XP target for the next level per the XP table in core rules.

## 9. Present the Updated Character

Display the full updated character sheet showing all changes highlighted. Save the updated character file.

End with: *"You feel stronger, sharper, more capable. The road ahead holds new challenges worthy of your growing power."*

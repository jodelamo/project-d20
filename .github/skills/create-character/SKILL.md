---
name: create-character
description: Guide the player through creating a new RPG character with race, class, attributes, skills, and backstory. Use this when the player wants to create or roll a new character.
---

# Character Creation Wizard

Guide the player through creating a new character step by step. **Roll dice where indicated.** Always show rolls.

## Step 1: Name & Concept

Ask the player for:
- **Character name**
- **Brief concept** (e.g., "a grizzled dwarven blacksmith turned adventurer")

If they want random generation, roll on improvised tables.

## Step 2: Choose Race

Present the available races from the core rules with their bonuses and traits (refer to RULES.md for full details):
- Dwarf (+2 CON, darkvision, poison resistance — subrace: Hill or Mountain)
- Elf (+2 DEX, darkvision, Fey Ancestry, Keen Senses — subrace: High or Wood)
- Halfling (+2 DEX, Lucky, Brave, Nimbleness — subrace: Lightfoot or Stout)
- Human (+1 all attributes, extra language)
- Dragonborn (+2 STR, +1 CHA, breath weapon — choose draconic ancestry)
- Gnome (+2 INT, darkvision, Gnome Cunning — subrace: Forest or Rock)
- Half-Elf (+2 CHA, +1 to two others, darkvision, Fey Ancestry, 2 extra skill proficiencies)
- Half-Orc (+2 STR, +1 CON, darkvision, Menacing, Relentless Endurance, Savage Attacks)
- Tiefling (+2 CHA, +1 INT, darkvision 60ft, fire resistance, Infernal Legacy)

If Dragonborn, also ask for **draconic ancestry** (Black/acid, Blue/lightning, Brass/fire, Bronze/lightning, Copper/acid, Gold/fire, Green/poison, Red/fire, Silver/cold, White/cold).

If the race has subraces (Dwarf, Elf, Halfling, Gnome), ask the player to choose.

## Step 3: Choose Class

Present the classes with a one-line pitch:
- **Barbarian** — Primal warrior. Rages for devastating power, toughest HP.
- **Bard** — Jack of all trades. Inspiration, magic, and charm.
- **Cleric** — Divine healer and protector. Spells from the gods.
- **Druid** — Nature's guardian. Wild Shape and primal magic.
- **Fighter** — Master of weapons and armor. High HP, devastating attacks.
- **Monk** — Martial artist. Unarmored speed, ki-powered strikes.
- **Paladin** — Holy knight. Divine Smite, healing, and oaths.
- **Ranger** — Wilderness expert. Half-caster with martial prowess.
- **Rogue** — Stealthy striker. Sneak attack damage, skills galore.
- **Sorcerer** — Innate magic. Metamagic to reshape spells.
- **Warlock** — Pact-bound caster. Eldritch power from a patron.
- **Wizard** — Arcane scholar. Largest spell list, spellbook mastery.

## Step 4: Roll Attributes

Use the **4d6 drop lowest** method for each of the 6 attributes:
1. Roll 4d6 for each attribute
2. Drop the lowest die
3. Sum the remaining 3
4. Repeat for all 6 attributes
5. Let the player **assign** the 6 results to STR, DEX, CON, INT, WIS, CHA
6. **Apply racial bonuses** after assignment

Show every roll: `🎲 Attribute roll: [d1, d2, d3, d4] → drop [lowest] → total [sum]`

If the player prefers, offer **standard array** instead: 15, 14, 13, 12, 10, 8

## Step 5: Calculate Derived Stats

- **HP**: Max hit die value + CON modifier
- **AC**: Based on starting equipment (see class defaults)
- **Initiative**: DEX modifier
- **Proficiency Bonus**: +2 (level 1)

## Step 6: Choose Skill Proficiencies

Each class grants a number of skills chosen from a specific list. The player's background also grants 2 additional proficiencies. Refer to RULES.md for the full skill list and class skill options.

Grant **class skill proficiencies**:
- Barbarian: Choose 2 from Animal Handling, Athletics, Intimidation, Nature, Perception, Survival
- Bard: Choose any 3 skills
- Cleric: Choose 2 from History, Insight, Medicine, Persuasion, Religion
- Druid: Choose 2 from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival
- Fighter: Choose 2 from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival
- Monk: Choose 2 from Acrobatics, Athletics, History, Insight, Religion, Stealth
- Paladin: Choose 2 from Athletics, Insight, Intimidation, Medicine, Persuasion, Religion
- Ranger: Choose 3 from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, Survival
- Rogue: Choose 4 from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, Stealth
- Sorcerer: Choose 2 from Arcana, Deception, Insight, Intimidation, Persuasion, Religion
- Warlock: Choose 2 from Arcana, Deception, History, Intimidation, Investigation, Nature, Religion
- Wizard: Choose 2 from Arcana, History, Insight, Investigation, Medicine, Religion

Then ask for a **background** (Acolyte, Criminal, Folk Hero, Noble, Sage, Soldier, or custom) which grants 2 more skill proficiencies per the background description.

## Step 7: Starting Equipment & Gold

Roll starting gold and assign equipment per the tables in `starting-equipment.md`.

## Step 8: Spells (if spellcaster)

For casters at level 1, refer to the starting spells table in `starting-equipment.md` for cantrip/spell counts by class. Generate spell options appropriate to the character concept and let the player choose.

## Step 9: Backstory

Ask the player to provide a backstory, or offer to **generate one** using the following prompts:
- Where did you grow up?
- What drove you to adventure?
- Who do you care about?
- What is your greatest fear?
- Do you have a rival or enemy?

Weave answers into a 2–3 paragraph backstory.

## Step 10: Save Character

Create the character file at `characters/{name-slug}.json` following the core rules format. Include all stats, inventory, spells, and backstory.

Present the completed character as an ASCII character sheet using the template below, then ask: *"Your hero is ready. Shall we begin the adventure?"*

### ASCII Character Sheet Template

Use horizontal rules (`═` for top/bottom, `─` for sections) with no side borders — just left-indented content. Substitute `{placeholders}` with real values. For the HP bar, render `█` blocks scaled to ~20 chars max. Only include the SPELLS section for caster classes.

```
═══════════════════════════════════════════════════════
                   ~ CHARACTER SHEET ~
═══════════════════════════════════════════════════════
  Name:  {name}
  Race:  {race}              Class: {class}
  Level: {level}             XP:    {xp} / {xp_next}

  HP: {bar} {current}/{max}
  AC: {ac}    Initiative: {init}    Prof. Bonus: {prof}
  Hit Die: {die}    Saves: {save1}, {save2}
───────────────────────────────────────────────────────
  ATTRIBUTES
  STR {s} ({m})   DEX {s} ({m})   CON {s} ({m})
  INT {s} ({m})   WIS {s} ({m})   CHA {s} ({m})
───────────────────────────────────────────────────────
  SKILLS (* = proficient)
  *{skill} {bonus}       *{skill} {bonus}
  ...
───────────────────────────────────────────────────────
  EQUIPMENT
  {item}
  ...
───────────────────────────────────────────────────────
  GOLD: {gold} GP
───────────────────────────────────────────────────────
  SPELLS (casters only)
  Cantrips: {cantrip_list}
  1st ({slots}): {spell_list}
───────────────────────────────────────────────────────
  RACIAL TRAITS
  {trait1}, {trait2}, {trait3}
───────────────────────────────────────────────────────
  BACKSTORY
  {wrapped backstory text}
═══════════════════════════════════════════════════════
```

**Formatting rules:**
- Prefix proficient skills with `*`, list them first
- Wrap backstory text at ~50 characters per line
- Omit the SPELLS section entirely for non-caster classes (Fighter, Barbarian, Rogue, Monk)

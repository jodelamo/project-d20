---
name: loot
description: Generate treasure, magical items, and loot drops for combat, treasure hoards, and hidden caches. Use this when generating loot or the player searches for treasure.
---

# Loot & Treasure Generation

Generate appropriate loot for combat drops, treasure hoards, and hidden caches.

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load context (party level, location, source)
- [ ] 2. Roll on loot tables from loot-tables.md
- [ ] 3. Generate unique/story items (if applicable)
- [ ] 4. Present loot narratively and mechanically
- [ ] 5. Update state (inventory, gold, campaign notes)
```

## 1. Context

Read the character and campaign files. Consider:
- Party level (scales loot quality)
- Location type (dungeon, wilderness, town)
- Source (monster drop, treasure chest, quest reward, hidden cache)

## 2. Roll on Loot Tables

Use the tables in `loot-tables.md` to generate loot:
- **Individual drops**: Roll d100 per defeated enemy on the CR-appropriate table
- **Treasure hoards**: Roll multiple times (gold, gems, items, special)
- **Magical items**: Roll rarity, type, and properties using the generation tables
- **Cursed items**: 5% chance any magical item is cursed (roll d6 for curse type)

## 3. Unique/Story Items

For quest rewards or major discoveries, generate a **named item** with:
- A proper name (e.g., "Frostbane, the Winter's End")
- A paragraph of lore
- A primary power and a secondary power
- A condition or restriction
- Connection to the campaign's story

## 4. Present the Loot

Describe the loot narratively:
*"Amid the fallen goblin's possessions, you find a leather pouch containing 14 gold pieces, and — glinting beneath a tattered cloak — a dagger with runes etched along the blade that pulse with faint blue light..."*

Then list mechanically using the item icons from RULES.md § "Display Formatting — Icons & Items":
```
📦 Loot Found:
  🪙 **14 GP**
  ✨⚔️ **Frostfang Dagger** (uncommon) — +1 dagger, +1d4 cold damage
```

## 5. Update State

- Add items and gold to character inventory (display with category icons per RULES.md § "Display Formatting")
- If item is plot-relevant, note it in campaign file
- Prompt player: keep, equip, or stash?

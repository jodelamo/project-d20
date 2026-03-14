---
name: new-campaign
description: Generate a new campaign world with setting, factions, locations, and a starting quest. Use this when the player wants to start a new campaign or generate a world.
---

# New Campaign — World Generation

You are creating a **brand new campaign world** for Project D20. Follow these steps:

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Ask player preferences (tone, setting hook, world size)
- [ ] 2. Generate the world (name, era, conflict, magic level, locations, factions, quest hook)
- [ ] 3. Save campaign state file
- [ ] 4. Prompt character creation
```

## Step 1: Ask the Player for Preferences

Use the `ask_user` tool to ask the player **one question at a time**. Always pass choices as a **list** (array), never a single string.

1. **Tone** — ask with these choices:
   - "Dark & gritty"
   - "Heroic fantasy"
   - "Lighthearted adventure"
   - "Horror"
   - "Surprise me"

2. **Setting hook** — ask with these choices:
   - "Ancient evil awakening"
   - "Warring kingdoms"
   - "Frontier exploration"
   - "Planar rifts"
   - "Surprise me"

3. **World size** — ask with these choices:
   - "Focused (single region)"
   - "Medium (kingdom-scale)"
   - "Epic (continent / multi-plane)"
   - "Surprise me"

If the player says "Surprise me" for any question, generate that choice randomly using dice:
- d4 for tone, d4 for setting hook, d4 for world size

## Step 2: Generate the World

Create the following and **narrate it dramatically** to the player:

### The World
- **Name**: A evocative, original world name
- **Era**: What age or period the world is in
- **Core conflict**: The central tension driving the world
- **Magic level**: Low (rare and feared), Medium (known but controlled), High (pervasive and common)

### Starting Region (3–5 locations)
For each location, generate:
- Name and type (town, dungeon, forest, ruins, etc.)
- Brief description (2–3 sentences)
- Notable feature or secret
- Danger level (safe / moderate / dangerous / deadly)

### Factions (2–4)
For each faction:
- Name and symbol
- Goals and methods
- Attitude toward the player (friendly / neutral / hostile / unknown)
- Key NPC leader (name, race, class, alignment, personality in one line)

### Starting Quest Hook
A compelling reason for an adventurer to be here right now. Include:
- Who needs help (or what mystery calls)
- What's at stake
- A ticking clock element

## Step 3: Save the Campaign

Create the campaign state file at `campaigns/{campaign-name-slug}.json` following the format defined in `rules/state-formats.md`. Populate all generated world data.

## Step 4: Prompt Character Creation

After presenting the world, ask: *"Your world awaits. Shall we create your character?"*

If yes, guide them to use the **create-character** skill.

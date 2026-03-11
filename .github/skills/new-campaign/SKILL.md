---
name: new-campaign
description: Generate a new campaign world with setting, factions, locations, and a starting quest. Use this when the player wants to start a new campaign or generate a world.
---

# New Campaign — World Generation

You are creating a **brand new campaign world** for Infinite RPG. Follow these steps:

## Step 1: Ask the Player for Preferences

Use the `ask_user` tool to ask the player **one question at a time**. Always pass choices as a **list** (array), never a single string.

1. **Tone** — ask with these choices:
   - "Dark & gritty"
   - "Heroic fantasy"
   - "Lighthearted adventure"
   - "Horror"
   - "Surprise me"

2. **Setting hook** — ask as freeform (no choices array): "Any themes you'd like? e.g. ancient evil awakening, warring kingdoms, frontier exploration, planar rifts"

3. **World size** — ask with these choices:
   - "Focused (single region)"
   - "Medium (kingdom-scale)"
   - "Epic (continent / multi-plane)"

If the player says "surprise me," generate everything randomly using dice:
- d4 for tone, d6 for theme, d4 for scale

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
- Key NPC leader (name, race, class, personality in one line)

### Starting Quest Hook
A compelling reason for an adventurer to be here right now. Include:
- Who needs help (or what mystery calls)
- What's at stake
- A ticking clock element

## Step 3: Save the Campaign

Create the campaign state file at `campaigns/{campaign-name-slug}.json` following the format defined in the core rules. Populate all generated world data.

## Step 4: Prompt Character Creation

After presenting the world, ask: *"Your world awaits. Shall we create your character?"*

If yes, guide them to use the **create-character** prompt.

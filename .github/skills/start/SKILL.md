---
name: start
description: Start an infinite autonomous campaign that auto-generates the world, characters, and plays through randomized adventures indefinitely. Use this when the player wants to watch an endless D&D campaign unfold automatically.
---

# Infinite Auto-Play Campaign

Run an autonomous, never-ending D&D campaign. The GM generates or resumes a world, creates or picks up a character, then plays through an infinite loop of randomized adventures — exploring, fighting, resting, shopping, traveling, and meeting NPCs — making all decisions via dice rolls, until the player stops the process.

## Table of Contents

- [Workflow Checklist](#workflow-checklist)
- [1. Load or Create Game State](#1-load-or-create-game-state)
- [2. Adventure Loop](#2-adventure-loop)
- [3. Decision Engine](#3-decision-engine)
- [4. Scene Resolution](#4-scene-resolution)
- [5. Character Death](#5-character-death)
- [6. Loop Control](#6-loop-control)

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load existing campaign & character — OR generate new ones
- [ ] 2. Enter the infinite adventure loop
- [ ] 3. (Loop) Roll on the Decision Engine to pick the next scene type
- [ ] 4. (Loop) Execute the scene using the appropriate skill
- [ ] 5. (Loop) Check character status (HP, resources, death)
- [ ] 6. (Loop) Repeat from step 3 — forever
```

## 1. Load or Create Game State

### Check for Existing State

Read the `campaigns/` and `characters/` directories.

**If campaign and character files exist:**
- List all available campaigns and characters to the player
- Ask the player: *"Pick up an existing campaign, or start fresh?"*
- If resuming: Load the campaign and character JSON files, read the session log, and narrate a brief recap of where things stand — current location, active quests, HP, level, gold, time of day
- Then proceed directly to **Step 2: Adventure Loop**

**If no files exist (or player chooses fresh):**
- Execute the **new-campaign** skill with all preferences set to "Surprise me" (roll dice for tone, setting hook, and world size)
- Then execute the **create-character** skill with all choices randomized via dice rolls (race, class, attributes, background — all rolled, no player input)
- Save both files, then proceed to **Step 2: Adventure Loop**

## 2. Adventure Loop

This is the **infinite core loop**. After every scene resolves, immediately roll for the next one. Never stop or ask the player what to do — the character acts autonomously based on dice rolls.

The loop repeats this cycle endlessly:

```
LOOP START
  |
  +-> Roll on Decision Engine (Step 3)
  +-> Resolve the scene using the matching skill (Step 4)
  +-> Update all state files (character + campaign JSON)
  +-> Check character status (Step 5)
  |     |
  |     +-> If dead: handle death (Step 5), then restart loop with new character
  |     +-> If alive: continue
  |
  +-> GOTO LOOP START
```

**Pacing:** After each scene, narrate a brief transitional beat (a moment of quiet, a shift in weather, time passing) before rolling the next scene. This keeps the narrative flowing naturally.

**Time Tracking:** Advance the in-game clock after every scene. Track day/night cycles. After 12-16 hours of in-game activity without rest, the character should prioritize resting (weight the Decision Engine toward rest).

## 3. Decision Engine

At the start of each loop iteration, roll to determine what happens next.

### Situational Modifiers

Before rolling, check the character's current state and apply **weighted overrides**:

| Condition | Override |
|-----------|----------|
| HP below 25% of max | Force **rest** or **shop** (for healing potions) — roll d6: 1-4 rest, 5-6 shop |
| 0 active quests | Weight toward **NPC encounter** (quest delivery) — add +3 to roll |
| Just finished combat | Skip combat this roll — reroll if combat comes up |
| 12+ hours without rest | Force **rest** |
| At a town/safe location | Allow **shop** and **NPC encounter** results |
| In wilderness / dungeon | Allow **combat** and **explore** results |
| New location just reached | Force **explore** before other actions |
| Level-up threshold reached | Force **level-up** before continuing |

### Main Decision Table (d20)

Roll d20 after applying situational overrides:

| d20   | Scene Type | Skill to Execute |
|-------|-----------|-----------------|
| 1-4   | **Combat Encounter** | Use the **combat** skill |
| 5-7   | **Exploration** | Use the **explore** skill |
| 8-9   | **NPC Encounter** | Use the **npc-encounter** skill |
| 10-11 | **Travel** | Use the **travel** skill (pick a destination from the campaign map, or generate a new one) |
| 12-13 | **Rest & Recovery** | Use the **rest** skill (short or long rest based on HP: below 50% = long rest, above = short rest) |
| 14    | **Shopping** | Use the **shop** skill (only if at a settlement; otherwise reroll) |
| 15    | **Magic Event** | Use the **magic** skill (arcane anomaly, wild magic surge, or ritual opportunity) |
| 16-17 | **Skill Challenge** | Use the **skill-check** skill (environmental obstacle, social test, or puzzle) |
| 18-19 | **Quest Progression** | Advance an active quest — pick the most urgent one, generate the next step, and resolve it using the appropriate skill |
| 20    | **Major Event** | Something dramatic happens — roll d6: 1-2 ambush by a powerful enemy (deadly combat), 3-4 discover a legendary location, 5 meet a major faction leader (NPC encounter), 6 find a treasure hoard (loot skill) |

### Autonomous Character Decisions

When a skill requires player choices (e.g., combat actions, dialogue options, shop purchases), the GM makes decisions **in character** based on:

1. **Class and abilities**: A wizard prefers spells, a fighter prefers melee, a rogue looks for stealth opportunities
2. **Personality**: Derived from the character's backstory and background
3. **Tactical sense**: Choose the mechanically smart option most of the time, but occasionally (on a d20 roll of 1-3) make a suboptimal but flavorful choice
4. **Resources**: Conserve spell slots and potions when HP is high; use them freely when things are desperate

For dialogue and social encounters, roll on this table to determine the character's approach:

| d6 | Approach |
|----|----------|
| 1  | Friendly and diplomatic (Persuasion) |
| 2  | Cautious and observant (Insight) |
| 3  | Boastful and entertaining (Performance) |
| 4  | Deceptive and cunning (Deception) |
| 5  | Direct and intimidating (Intimidation) |
| 6  | Honest and straightforward (no check, just talk) |

## 4. Scene Resolution

For every scene, follow this exact procedure:

1. **Narrate the setup** — describe what the character encounters, using vivid sensory detail
2. **Execute the matching skill** — follow its full workflow checklist step by step (load state, resolve actions, update state)
3. **Show all dice rolls** — every roll is visible in the standard format: `d20 rolled: [Result] + [Modifier] = [Total] vs DC [Target]`
4. **Narrate the outcome** — describe what happened, how the character reacts, and what changes
5. **Update state files** — write to character and campaign JSON after every scene
6. **Transition** — brief narrative bridge to the next scene

### Skill Chaining

Follow all natural skill chains as defined in each skill:
- **Combat** chains to **loot**, which may chain to **level-up**
- **Explore** may chain to **npc-encounter**, **loot**, or **combat** (traps/ambushes)
- **Travel** may chain to **combat** (random encounters) or **explore** (new locations)
- **NPC encounter** may chain to **quest progression** or **shop**

Let chains resolve fully before rolling the next Decision Engine result.

## 5. Character Death

Death is real and permanent. When a character dies:

1. **Narrate the death solemnly** — honor the fallen character
2. **Record the death** in the campaign session log with cause, location, and level reached
3. **Generate a new character** immediately using the **create-character** skill with all choices randomized
4. **Narrative hook**: The new character arrives at the same location through a dice-rolled circumstance:

| d6 | How the New Character Arrives |
|----|-------------------------------|
| 1  | Was already nearby, drawn by the sounds of the previous battle |
| 2  | A traveling adventurer passing through, stumbles upon the scene |
| 3  | Sent by a faction or NPC who learned of the previous character's fate |
| 4  | Emerges from a nearby dungeon or cave, seeking daylight |
| 5  | A prisoner or captive just freed from a nearby threat |
| 6  | Wakes up with amnesia at the location, no memory of how they got there |

5. **Continue the campaign** — the world persists, quests remain active, NPCs remember the fallen character
6. **Resume the Adventure Loop** from Step 2

## 6. Loop Control

This campaign runs **infinitely**. The GM never stops to ask "What do you want to do?" — instead, the Decision Engine drives all action automatically.

**The only way to stop is for the player to interrupt or abort the process.**

### Session Pacing

- Keep scenes varied — the Decision Engine's weighted modifiers prevent repetitive sequences
- Aim for a rhythm: action, exploration, social, rest — with twists from Major Events
- Every 5-10 scenes, introduce a narrative thread that connects recent events (a recurring villain, a building mystery, a faction conflict escalating)
- Track the campaign's evolving story in the session log

### Narrative Continuity

Even though scenes are randomized, maintain coherent storytelling:
- Reference previous events in narration ("The scar from yesterday's goblin ambush still aches...")
- Have NPCs react to the character's growing reputation
- Advance active quests naturally — don't let them stagnate
- Evolve the world state — factions act, weather changes, time passes, seasons shift

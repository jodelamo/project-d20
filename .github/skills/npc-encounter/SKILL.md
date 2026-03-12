---
name: npc-encounter
description: Generate memorable NPCs and handle social interactions, dialogue, and persuasion. Use this when the player meets or interacts with an NPC.
---

# NPC Encounter

Generate memorable NPCs and handle social interactions.

## 1. Load State

Read campaign and character files to understand:
- Current location and its inhabitants
- Known NPCs in this area
- Active quests and faction relationships
- Character's social skills (Persuasion, Deception, Intimidation, Insight, Performance)

## 2. NPC Generation (if new)

Roll on the tables in `npc-tables.md` for race, disposition, personality quirk, and secret.

Generate: name, occupation, appearance (2 sentences), motivation, and key information they possess.

## 3. Introduce the NPC

Narrate the encounter dramatically. Describe:
- How the NPC appears or approaches
- Their body language and demeanor
- What they're doing when the player finds them
- Any immediately obvious details

## 4. Dialogue

Role-play the NPC in character. Maintain their personality, quirk, and disposition consistently.

### Social Skill Checks

When the player attempts to influence the NPC:

**Persuasion** (CHA) — Honest appeal, reasoning, charm
- DC based on how unreasonable the request is and NPC disposition
- Friendly NPCs: DC lowered by 5
- Hostile NPCs: DC raised by 5

**Deception** (CHA) — Lying, bluffing, misleading
- Opposed check: Player's Deception vs NPC's Insight
- If NPC catches the lie, disposition worsens

**Intimidation** (CHA or STR) — Threats, displays of power
- DC based on NPC's courage and the threat's credibility
- Success: NPC complies but disposition drops
- Failure by 5+: NPC becomes hostile

**Insight** (WIS) — Reading the NPC
- Player's Insight vs NPC's Deception (if lying) or DC 15 (to read mood/intent)
- Success: Reveal a clue about the NPC's true feelings or secret
- Critical success (beat by 10+): Reveal the NPC's secret

**Performance** (CHA) — Entertaining, impressing
- Success can improve disposition by 1 step
- Critical success: NPC becomes a fan, offers a reward

### Disposition Shifts
Track disposition changes. If the player is consistently kind/helpful, shift up. If aggressive/rude, shift down. Save to campaign file.

## 5. Quest Delivery

If the NPC has a quest to offer:
1. Foreshadow it in dialogue naturally (don't just dump it)
2. Present the problem and what they need
3. Negotiate reward (player can haggle — Persuasion check)
4. Record the quest in the campaign file under `quests.active`

Quest format:
```json
{
  "name": "Quest Title",
  "giver": "NPC Name",
  "description": "What needs to be done",
  "reward": "Gold, items, information, or favor",
  "deadline": "Urgent / 3 days / no deadline",
  "status": "active"
}
```

## 6. Information Trading

NPCs can share:
- **Free info**: Common knowledge, obvious directions
- **Persuasion DC 10**: Rumors, opinions, local gossip
- **Persuasion DC 15**: Useful intel, warnings, hidden paths
- **Persuasion DC 20**: Secrets, faction plans, treasure locations
- **Bribery**: Offering gold reduces DC by 1 per 5 GP offered

## 7. Recurring NPCs

When an NPC is memorable or quest-related, save them to the campaign file:
```json
{
  "name": "NPC Name",
  "race": "...",
  "occupation": "...",
  "location": "...",
  "disposition": "friendly",
  "quirk": "...",
  "secret": "...",
  "quests_given": [],
  "relationship_notes": "Helped the party, owes them nothing currently"
}
```

## 8. Update State

- Save new NPCs to campaign file
- Update NPC dispositions if changed
- Record new quests
- Award XP for meaningful social encounters (25–100 XP)
- Advance time appropriately (conversations take 5–30 minutes)

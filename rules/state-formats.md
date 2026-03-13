# Game State File Formats

## Character Sheet Format (`characters/{name}.json`)

```json
{
  "name": "Character Name",
  "race": "Human",
  "subrace": null,
  "class": "Fighter",
  "level": 1,
  "xp": 0,
  "xp_next": 300,
  "hp": { "current": 12, "max": 12 },
  "ac": 16,
  "attributes": {
    "STR": 16, "DEX": 12, "CON": 14,
    "INT": 10, "WIS": 8, "CHA": 13
  },
  "proficiency_bonus": 2,
  "skills": {
    "Athletics": "proficient",
    "Intimidation": "proficient",
    "Perception": "none"
  },
  "saving_throws": ["STR", "CON"],
  "inventory": [],
  "gold": 15,
  "spells": { "known": [], "slots": {}, "cantrips": [] },
  "conditions": [],
  "death_saves": { "successes": 0, "failures": 0 },
  "features": [],
  "backstory": "",
  "notes": ""
}
```

## Campaign State Format (`campaigns/{campaign-name}.json`)

```json
{
  "name": "Campaign Name",
  "setting": "Brief world description",
  "current_location": "Starting Town",
  "party": ["character1.json"],
  "session_log": [],
  "world": {
    "locations": {},
    "factions": {},
    "npcs": {},
    "quests": { "active": [], "completed": [] }
  },
  "time": { "day": 1, "hour": 8, "weather": "clear" }
}
```

## Updating State

After every significant event (combat, rest, shopping, level-up, quest progress), **update the relevant JSON files** using the file tools. Always read the current state before modifying.

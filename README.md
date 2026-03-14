# 🎲 Project D20

A fully AI-driven tabletop RPG campaign system powered by **GitHub Copilot**, built on the rules of **Dungeons & Dragons** (5th Edition Basic Rules, 2014). **100% prompt-engineered** — no application code, no framework, no build step. Just markdown instructions, dice, and imagination.

## Requirements

This project runs entirely through an AI coding agent. You will need one of the following:

- [OpenCode](https://opencode.ai/) (recommended)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot)
- Any similar AI coding agent that supports custom instructions and tool use

## How to Play

Open this project in your agent of choice and start a chat session. The game is played entirely through conversation. Skills are registered as slash commands — just type `/skill-name` to use them.

### Getting Started

#### Infinite Auto-Play

Type `/start` and watch an entire D&D campaign unfold on its own. The GM will generate (or resume) a world and a **party of adventurers**, then play through an endless sequence of combat, exploration, travel, NPC encounters, shopping, rest, and more — all driven by dice rolls. It runs forever until you stop it.

- Fresh start? It creates a random world and a full party for you.
- Existing campaign? It picks up right where you left off.

#### Manual Play

Prefer to drive the story yourself? Set things up step by step:

1. Use `/new-campaign` to generate your world
2. Use `/create-character` to build your hero
3. Start adventuring by using the relevant skill command for each action!

### Available Skills

| Skill | Command | What it does |
|-------|---------|-------------|
| **Start** | **`/start`** | **🎲 Launch an infinite autonomous campaign — the primary way to play** |
| New Campaign | `/new-campaign` | 🌍 Generate a new world, setting, factions, and starting quest |
| Create Character | `/create-character` | 🧝 Create a character with race, class, attributes, and skills |
| Explore | `/explore` | 🔍 Explore your surroundings, search for secrets, investigate |
| Combat | `/combat` | ⚔️ Fight enemies with initiative, attacks, and tactical combat |
| Skill Check | `/skill-check` | 🎯 Roll for any ability or skill test |
| Magic | `/magic` | ✨ Cast spells and use magical abilities |
| NPC Encounter | `/npc-encounter` | 🗣️ Meet and interact with NPCs |
| Shop | `/shop` | 🛒 Buy, sell, and trade at merchants |
| Rest | `/rest` | 🏕️ Take a short or long rest to recover |
| Level Up | `/level-up` | ⬆️ Level up and gain new abilities |
| Loot | `/loot` | 💰 Generate treasure and magical items |
| Travel | `/travel` | 🗺️ Journey between locations with random encounters |

### Game System

- **D&D 5e Basic Rules (2014)** — faithful d20 system with 6 core attributes
- **9 playable races**: Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling
- **12 classes**: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
- **18 skills** with proficiency and expertise
- **XP-based leveling** with class features up to level 10
- **Full spellcasting** system with spell slots, cantrips, and Pact Magic
- **Every outcome determined by dice** — shown in the open

### Game State

Your game state is persisted as files:
- `characters/` — Character sheets (JSON)
- `campaigns/` — Campaign world state (JSON)

These files are read and updated automatically as you play.

### Tips

- The full game rules are in `RULES.md` — Copilot loads them automatically via custom instructions
- You can say anything — the skills handle the mechanics, but you drive the story
- Be creative! Propose unorthodox solutions and the GM will set a fair DC
- Your choices have consequences that persist in the campaign file
- Death is real — play smart or roll lucky 🎲

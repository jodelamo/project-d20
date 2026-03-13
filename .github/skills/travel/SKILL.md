---
name: travel
description: Handle journeys between locations with travel events, random encounters, and world-building. Use this when the player wants to travel or journey to a new location.
---

# Overworld Travel

Handle journeys between locations with travel events, random encounters, and world-building.

## Workflow Checklist

Copy this checklist and mark each step complete as you go:

```
- [ ] 1. Load state (location, destination, supplies, time, weather)
- [ ] 2. Determine travel distance, terrain, and weather
- [ ] 3. Narrate the journey (atmosphere, time passing)
- [ ] 4. Roll random encounters per travel segment
- [ ] 5. Track resources (rations, water, light, navigation)
- [ ] 6. Describe arrival and generate new location (if needed)
- [ ] 7. Update state (location, rations, time, discoveries, XP, HP)
```

## 1. Load State

Read campaign and character files for:
- Current location and destination
- Known map locations and routes
- Party supplies (rations, water, torches)
- Time of day and weather
- Character's Survival, Perception, and Nature skills

## 2. Determine Travel Details

If the route is known, use the campaign data. If new, roll on the distance, terrain, and weather tables in `encounters.md`.

## 3. Travel Narration

Describe the journey in atmospheric prose:
- The terrain and scenery changing
- The time of day shifting (dawn → midday → dusk → night)
- Sounds, smells, and wildlife
- How the character feels

Break multi-day journeys into segments with narration for each.

## 4. Random Encounters (per travel segment)

Roll d20 for each half-day of travel on the appropriate table in `encounters.md` (Road, Wilderness, or Dangerous Territory).

## 5. Resource Management

### Rations
Each character consumes **1 ration per day**. Track rations:
- If rations run out, must forage: **Survival DC 10** for d4 rations (takes 1 hour)
- Failure: No food. After 3 + CON modifier days without food, gain 1 exhaustion per day

### Water
In hot or desert terrain, require **2 waterskins per day** or CON save DC 15 or gain exhaustion.

### Torches / Light
In dark areas (caves, nighttime forest), require a light source:
- Torch: 1 hour, bright 20ft, dim 20ft
- Lantern: 6 hours per oil flask
- Darkvision: Characters with darkvision are fine in dim light

### Navigation
In unfamiliar territory without a road:
- **Survival DC 12**: Stay on course
- **Failure**: Add d4 hours, possibly encounter something unexpected
- **Failure by 5+**: Lost. Must make another check to reorient, or backtrack

## 6. Arrival

When the party arrives at the destination:
1. Describe the approach (what they see from a distance)
2. Note the time of arrival and current weather
3. Present immediate options (enter the town, scout the area, make camp)
4. Update the campaign file with the new location

If it's a new location, generate it:
- Name, type, size
- Notable features (3–5)
- Inhabitants and atmosphere
- Potential hooks and dangers

## 7. Update State

After travel:
- Update current location in campaign file
- Deduct rations consumed
- Update time (hours/days elapsed)
- Record any new locations discovered
- Record any encounters and their outcomes
- Award XP for travel encounters and discoveries
- Update HP if any damage occurred during travel

---
name: shop
description: Handle buying, selling, and trading at merchants and shops. Use this when the player wants to visit a shop or trade items.
---

# Shop & Trading

Handle all buying, selling, and trading interactions.

## 1. Load State

Read character file for: gold, inventory, CHA modifier, Persuasion skill.
Read campaign file for: current location and known merchants.

## 2. Generate a Shop (if new)

### Shop Type (d8)
| d8 | Shop |
|----|------|
| 1 | General Store — adventuring supplies, rations, rope |
| 2 | Blacksmith — weapons and armor |
| 3 | Apothecary — potions, herbs, antidotes |
| 4 | Arcanist — scrolls, components, magical curiosities |
| 5 | Tavern — food, drink, rooms, rumors |
| 6 | Fence — stolen goods, questionable items, information |
| 7 | Exotic Trader — rare materials, foreign goods, pets |
| 8 | Wandering Merchant — random assortment, unique items |

Generate the merchant as an NPC with personality and describe the shop's atmosphere.

## 3. Inventory Generation

Use the inventories and price lists in `price-list.md` for standard stock (General Store, Blacksmith, Apothecary, Arcanist) and the special stock rarity table.

## 4. Buying

1. Player selects items
2. Calculate total cost
3. If player can afford it: deduct gold, add items to inventory
4. If player can't afford it: merchant says so, suggest haggling

## 5. Selling

Players can sell items at **half their base value** (round down).

Merchants will only buy items relevant to their shop type. A blacksmith won't buy potions.

## 6. Haggling

Player can attempt to get a better price:

**Persuasion check:**
- **DC 15**: 10% discount (buying) or 10% bonus (selling)
- **DC 20**: 20% discount/bonus
- **DC 25**: 30% discount/bonus (merchant's best offer)
- **Failure by 5+**: Merchant is offended, refuses to deal for the rest of the visit

**Deception check** (lying about item value):
- Same DCs as Persuasion
- If caught (merchant's Insight beats Deception): banned from the shop

Each player gets **one haggle attempt per transaction**.

## 7. Special Services

Some shops offer services:
- **Blacksmith**: Repair equipment (10% of item value), commission custom weapons (double price, 1d4 days)
- **Arcanist**: Identify magical items (25 GP), enchant items (varies)
- **Apothecary**: Cure disease (50 GP + Medicine check), brew custom potions (varies)

## 8. Update State

- Update character gold and inventory
- Save shop and merchant to campaign file for future visits
- Shop inventories refresh after d4 days of in-game time

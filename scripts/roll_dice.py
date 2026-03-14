#!/usr/bin/env python3
"""Dice roller for Project D20.

Usage:
    python scripts/roll_dice.py <dice_notation> [<dice_notation> ...]

Examples:
    python scripts/roll_dice.py d20
    python scripts/roll_dice.py 2d6
    python scripts/roll_dice.py d4 d4 d4
    python scripts/roll_dice.py 3d8+5
"""

import random
import re
import sys


def roll(notation: str) -> dict:
    """Parse and roll dice notation like '2d6+3' or 'd20'.

    Returns a dict with keys: notation, rolls, modifier, total.
    """
    match = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", notation.strip().lower())
    if not match:
        raise ValueError(f"Invalid dice notation: {notation}")

    count = int(match.group(1)) if match.group(1) else 1
    sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + modifier

    return {
        "notation": notation,
        "rolls": rolls,
        "modifier": modifier,
        "total": total,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/roll_dice.py <dice_notation> [...]")
        print("Example: python scripts/roll_dice.py d20 2d6+3")
        sys.exit(1)

    for notation in sys.argv[1:]:
        result = roll(notation)
        rolls_str = ", ".join(str(r) for r in result["rolls"])
        mod_str = f" + {result['modifier']}" if result["modifier"] > 0 else (
            f" - {abs(result['modifier'])}" if result["modifier"] < 0 else ""
        )
        print(f"\U0001f3b2 {result['notation']} rolled: [{rolls_str}]{mod_str} = {result['total']}")


if __name__ == "__main__":
    main()

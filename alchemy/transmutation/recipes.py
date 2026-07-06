from ..potions import strength_potion
from alchemy.elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to " +
            f"Gold: brew ’{create_air()}’ and " +
            f"’{strength_potion()}’ " +
            f"mixed with ’{create_fire()}’")

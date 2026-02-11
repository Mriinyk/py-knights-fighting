from app.knight_class import Knight
from app.knights_list import KNIGHTS


def battle(knightsconfig: dict) -> dict:
    lancelot = Knight(**knightsconfig["lancelot"])
    arthur = Knight(**knightsconfig["arthur"])
    mordred = Knight(**knightsconfig["mordred"])
    red_knight = Knight(**knightsconfig["red_knight"])

    result_1 = lancelot.battle(mordred)
    result_2 = arthur.battle(red_knight)

    return {**result_1, **result_2}


print(battle(KNIGHTS))

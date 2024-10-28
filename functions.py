from classes import *


charmander = Pokemon("Charmander", 100, {"Tackle" : 10, "Quick Attack": 12, "Ember": 14}, "Water", 2)
piplup = Pokemon("Piplup", 100, {"Tackle" : 10, "Quick Attack": 12, "Water Gun": 14}, "Fire", 1)

def battle(pokemon1, pokemon2):
    print(f"Battle Start! {pokemon1.get_name()} vs {pokemon2.get_name()}")

    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        print(f"{pokemon1.get_name()}'s turn.")
        pokemon2.take_damage(pokemon1.choose_move(), pokemon1.get_type_value())

        print(f"{pokemon2.get_name()}'s turn.")
        pokemon1.take_damage(pokemon2.choose_move(), pokemon2.get_type_value())

    if pokemon1.is_fainted():
        print(f"{pokemon1.get_name()} fainted.")
        print(f"{pokemon2.get_name()} Won the Battle!")

    else:
        print(f"{pokemon2.get_name()} fainted.")
        print(f"{pokemon1.get_name()} Won the Battle!")


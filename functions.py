from classes import *
import random


charmander = Pokemon("Charmander", 100, {"Tackle": (10, 0, 0), "Quick Attack": (12, 0, 1), "Ember": (14, 1, 0)}, "Water", 2, 10)
piplup = Pokemon("Piplup", 100, {"Tackle": (10, 0, 0), "Quick Attack": (12, 0, 1), "Water Gun": (14, 1, 0)}, "Fire", 1, 11)

def battle(pokemon1, pokemon2):
    print(f"Battle Start! {pokemon1.get_name()} vs {pokemon2.get_name()}")

    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        print(f"{pokemon1.get_name()}'s choice of move.")
        damage1, move_type1, pokemon_1, move_attacker_1, is_priority_1 = pokemon1.choose_move()

        print(f"{pokemon2.get_name()}'s choice of move.")
        damage2, move_type2, pokemon_2, move_attacker_2, is_priority_2 = pokemon2.choose_move()

        if is_priority_1 == 0 and is_priority_2 == 0:
            if pokemon1.get_speed() > pokemon2.get_speed():
                pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
                pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
            elif pokemon1.get_speed() < pokemon2.get_speed():
                pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
            else:
                result = random.choice([1, 2])
                if result == 1:
                    pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
                    pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                else:
                    pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                    pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
        else:
            if is_priority_1 == 1 and is_priority_2 == 0 :
                pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
                pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
            elif is_priority_1 == 0 and is_priority_2 == 1 :
                pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
            else:
                result = random.choice([1, 2])
                if result == 1:
                    pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())
                    pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                else:
                    pokemon1.take_damage(damage2, move_type2, pokemon_2, move_attacker_2, pokemon2.get_type_value())
                    pokemon2.take_damage(damage1, move_type1, pokemon_1, move_attacker_1, pokemon1.get_type_value())

    if pokemon1.is_fainted():
        print(f"{pokemon1.get_name()} fainted.")
        print(f"{pokemon2.get_name()} Won the Battle!")

    else:
        print(f"{pokemon2.get_name()} fainted.")
        print(f"{pokemon1.get_name()} Won the Battle!")


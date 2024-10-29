
poke_type_value = {
    1, #Water
    2, #Fire
    3, #Rock
    4  #Grass
}

poke_type = {
    "Water",
    "Fire",
    "Rock",
    "Grass"
}

moves = {
    "Tackle": (10, 0, 0),               # (damage, if_elemental 0 == no  1 == yes, if_priority_attack 0 == no  1 == yes)
    "Quick Attack": (12, 0, 1),
    "Thunderbolt": (14, 1, 0),
    "Ember": (14, 1, 0),
    "Water Gun": (14, 1, 0)
}

class Pokemon:
    def __init__(self, name, hp, moves, poke_type, poke_type_value, poke_speed):
        self.name = name
        self.hp = hp
        self.moves = moves
        self.poke_type = poke_type
        self.poke_type_value = poke_type_value
        self.poke_speed = poke_speed

        self.moves_list = list(self.moves.items())
        self.moves_list_damage = [move[0] for move in self.moves.values()]
        self.moves_list_typing = [move[1] for move in self.moves.values()]
        self.moves_list_priority = [move[2] for move in self.moves.values()]

    def get_type_value(self):
        return self.poke_type_value

    def get_name(self):
        return self.name

    def take_damage(self, damage, damage_type, pokemon_name_attacker, move_name, attacker_type):
        effectiveness = {
            (1, 1): 1,
            (1, 2): 0.5,
            (1, 3): 0.5,
            (1, 4): 1.5,

            (2, 1): 1.5,
            (2, 2): 1,
            (2, 3): 1.5,
            (2, 4): 0.5,

            (3, 1): 1.5,
            (3, 2): 0.5,
            (3, 3): 1,
            (3, 4): 1.5,

            (4, 1): 0.5,
            (4, 2): 1.5,
            (4, 3): 0.5,
            (4, 4): 1,
        }

        multiplier = effectiveness.get((self.poke_type_value, attacker_type))

        if damage_type == 1:
            adjusted_damage = damage * multiplier
        else:
            multiplier = 1
            adjusted_damage = damage

        self.hp -= adjusted_damage

        print(f"{pokemon_name_attacker} uses {move_name} on {self.name}")


        if multiplier == 1:
            print(f"Normal Effective damage on {self.name}!")
        elif multiplier == 0.5:
            print(f"Not Very Effective damage on {self.name}!")
        elif multiplier == 1.5:
            print(f"Very Effective damage on {self.name}!")

        print(f"{self.name} Hp reduced to {self.hp}\n")

    def heal(self):
        self.hp = self.hp + 20

    def is_fainted(self):
        return self.hp <= 0

    def get_speed(self):
        return self.poke_speed

    def choose_move(self):
        for index, (move, (damage, _, _)) in enumerate(self.moves_list, start=1):
            print(f"{index}, {move} - Damage: {damage} ")
        print("Input 1-3 to choose a move")

        choice = int(input("Enter your choice: ")) - 1

        damage = self.moves_list_damage[choice]
        type_value = self.moves_list_typing[choice]
        pokemon = self.name
        move_name = self.moves_list[choice][0]
        if_priority = self.moves_list_priority[choice]
        print("\n")

        return damage, type_value, pokemon, move_name, if_priority



    def display_info(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Moves: {self.moves}")
        print(f"Type: {self.poke_type}")
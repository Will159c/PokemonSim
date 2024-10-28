
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
    "Tackle": 10,
    "Quick Attack": 12,
    "Thunderbolt": 15,
    "Ember": 14,
    "Water Gun": 14
}

class Pokemon:
    def __init__(self, name, hp, moves, poke_type, poke_type_value):
        self.name = name
        self.hp = hp
        self.moves = moves
        self.poke_type = poke_type
        self.poke_type_value = poke_type_value

        self.moves_list = list(self.moves.items())
        self.moves_list_damage = list(self.moves.values())

    def get_type_value(self):
        return self.poke_type_value

    def get_name(self):
        return self.name

    def take_damage(self, damage, attacker_type):
        if damage == 14:
            if self.poke_type_value == 1 and attacker_type == 1:
                damage = damage
                self.hp -= damage
                print("Normal Effective")
            elif self.poke_type_value == 1 and attacker_type == 2:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")
            elif self.poke_type_value == 1 and attacker_type == 3:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")
            elif self.poke_type_value == 1 and attacker_type == 4:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")

            if self.poke_type_value == 2 and attacker_type == 1:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")
            elif self.poke_type_value == 2 and attacker_type == 2:
                damage = damage
                self.hp -= damage
                print("Normal Effective")
            elif self.poke_type_value == 2 and attacker_type == 3:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")
            elif self.poke_type_value == 2 and attacker_type == 4:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")

            if self.poke_type_value == 3 and attacker_type == 1:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")
            elif self.poke_type_value == 3 and attacker_type == 2:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")
            elif self.poke_type_value == 3 and attacker_type == 3:
                damage = damage
                self.hp -= damage
                print("Normal Effective")
            elif self.poke_type_value == 3 and attacker_type == 4:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")

            if self.poke_type_value == 4 and attacker_type == 1:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")
            elif self.poke_type_value == 4 and attacker_type == 2:
                damage = damage * 1.5
                self.hp -= damage
                print("Super Effective!")
            elif self.poke_type_value == 4 and attacker_type == 3:
                damage = damage / 2
                self.hp -= damage
                print("Not Very Effective")
            elif self.poke_type_value == 4 and attacker_type == 4:
                damage = damage
                self.hp -= damage
                print("Normal Effective")
        else:
            print("Normal Effective")
            self.hp -= damage

        print(f"Hp reduced to {self.hp}\n")

    def heal(self):
        self.hp = self.hp + 20

    def is_fainted(self):
        return self.hp <= 0

    def choose_move(self):
        for index, (move, damage) in enumerate(self.moves_list, start=1):
            print(f"{index}, {move} - Damage: {damage} ")
        print("Input 1-3 to choose a move")

        choice = int(input("Enter your choice: ")) - 1

        damage = self.moves_list_damage[choice]

        return damage;



    def display_info(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Moves: {self.moves}")
        print(f"Type: {self.poke_type}")
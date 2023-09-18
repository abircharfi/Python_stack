import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        damage = self.attack_power
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def take_damage(self, damage):
        self.hp -= damage

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=50, attack_power=10)
        self.spell_power = 20

    def cast_spell(self, other):
        damage = random.randint(self.spell_power - 5, self.spell_power + 5)
        other.take_damage(damage)
        print(f"{self.name} casts a spell on {other.name} for {damage} damage!")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=60, attack_power=15)
        self.defend_power = 10
        self.defending = False

    def defend(self):
        self.defending = True
        print(f"{self.name} prepares to defend against the next attack!")

    def take_damage(self, damage):
        if self.defending:
            damage -= self.defend_power
            self.defending = False
        super().take_damage(damage)

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, hp=45, attack_power=20)
        self.critical_chance = 0.2  # 20% chance for a critical hit

    def attack(self, other):
        if random.random() < self.critical_chance:
            damage = self.attack_power * 2  # Critical hit
            print(f"{self.name} lands a critical hit on {other.name} for {damage} damage!")
        else:
            damage = self.attack_power
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        other.take_damage(damage)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=55, attack_power=12)
        self.accuracy = 0.85  # 85% accuracy

    def attack(self, other):
        if random.random() < self.accuracy:
            damage = self.attack_power
            print(f"{self.name} shoots an arrow at {other.name} for {damage} damage!")
            other.take_damage(damage)
        else:
            print(f"{self.name} misses the shot!")

def choose_character_class():
    print("Choose your character class:")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")
    print("4. Archer")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def main():
    player_choice = choose_character_class()

    if player_choice == 1:
        player = Mage("Gandalf")
    elif player_choice == 2:
        player = Warrior("Aragorn")
    elif player_choice == 3:
        player = Rogue("Legolas")
    elif player_choice == 4:
        player = Archer("Robin Hood")
    else:
        print("Invalid choice. Defaulting to Mage.")
        player = Mage("Gandalf")

    enemies = [Mage("Saruman"), Warrior("Lurtz"), Rogue("Uruk-hai"), Archer("Ugluk")]

    current_player = player

    while any(enemy.is_alive() for enemy in enemies):
        enemy = random.choice([e for e in enemies if e.is_alive()])
        print(f"{player.name} (HP: {player.hp}) vs. {enemy.name} (HP: {enemy.hp})")
        print("What will you do?")
        choice = input("(A)ttack or use (S)pecial move: ").strip().lower()

        if choice == 'a':
            current_player.attack(enemy)
        elif choice == 's' and isinstance(current_player, Mage):
            current_player.cast_spell(enemy)
        elif choice == 's' and isinstance(current_player, Warrior):
            current_player.defend()
        else:
            print("Invalid choice. Try again.")
            continue

        current_player, enemy = enemy, current_player

        for enemy in enemies:
            if enemy.is_alive():
                enemy_choice = random.choice(['a', 's'])
                if enemy_choice == 'a':
                    current_player.attack(player)
                elif enemy_choice == 's' and isinstance(enemy, Mage):
                    enemy.cast_spell(player)
                elif enemy_choice == 's' and isinstance(enemy, Warrior):
                    enemy.defend()

    print("Game over!")
    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print("Enemies win!")

if __name__ == "__main__":
    main()
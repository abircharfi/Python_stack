import random

class Character:
    # Constructor
    def __init__(self, name, attack_power):
        # Instance Attributes
        self.name = name
        self.hp = 100
        self.attack_power = attack_power

    # Instance Method: check if player is alive.
    def is_alive(self):
        return self.hp > 0
    
    # Instance Method: Attack other players
    def attack(self, target):
        if self.is_alive():
            damage = self.attack_power
            actual_damage = target.take_damage(damage)
            print(f"{self.name} attacked {target.name} for {actual_damage} damage!")
        return self
    
    # Instance Method: Take damage.
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp} HP left.")
        return damage


# A Mage can cast a spell to deal extra damage
class Mage(Character):
    # Constructor
    def __init__(self, name, attack_power):
        # Using the parent's constructor to initialize 'name' and 'attack_power'.
        super().__init__(name, attack_power)
        # Initializing 'spell_power' which is unique to the Mage class.
        self.spell_power = 10

    # Instance Method: Steal HP from target.
    def cast_spell(self, target):
        if self.is_alive():
            damage = self.spell_power
            extra_hp = target.take_damage(damage)
            self.hp += extra_hp
            print(f"{self.name} cast a spell on {target.name} stealing {extra_hp} HP points!")
        return self

# A Warrior can defend to reduce incoming damage on the next turn.
class Warrior(Character):
    # Constructor
    def __init__(self, name, attack_power):
        # Using the parent's constructor to initialize 'name' and 'attack_power'.
        super().__init__(name, attack_power)
        # Initializing 'defend_power' and 'is_defending' which are unique to the Warrior class.
        self.defend_power = 10
        self.is_defending = False

    # Instance Method: Prepare for next turn
    def defend(self, other):
        damage =self.defend_power
        if self.is_alive():
            self.is_defending = True
            print(f"{self.name} prepares to defend against the next attack!")
            other.take_damage(damage)


# Instance Method: Overriding the parent 'take_damage' method to reduce the damage when the Warrior is defending!
    def take_damage(self, damage):
        if self.is_defending:
            damage -= self.defend_power
            if damage < 0:
                damage = 0
            self.is_defending = False
        super().take_damage(damage)
        return damage
# a Rogue can lands a critical hit to multiplicate the enemy damage    
class Rogue(Character):

    def __init__( self,name, attack_power):
        super().__init__(name, attack_power)
        self.critical_chance = 5 # 50% chance for a critical hit
        self.critical_power =10
        
    
    def Critical_hit(self, other):
        chance_c= random.randint(0, 9)
        damage = self.critical_power
        if chance_c < self.critical_chance:
            damage = self.critical_power * 2  # Critical hit
            print(f"{self.name} lands a critical hit on {other.name} for {damage} damage!")
        else:
            
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        other.take_damage(damage)
        
     


def choose_character_class():
    print("Choose your character :")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    player_choice = choose_character_class()

    if player_choice == 1:
        player = Mage("Mage",20)
        enemies = [Warrior("Warrior",6), Rogue("Rogue",10)]
    elif player_choice == 2:
        player = Warrior("Warrior",20)
        enemies = [Mage("Mage",8), Rogue("Rogue",10)]
    elif player_choice == 3:
        player = Rogue("Rogue",20)
        enemies = [Mage("Mage",8), Warrior("Warrior",8)]
    else:
        print("Invalid choice. Defaulting to Mage.")
        player = Mage("Mage",8)

    current_player = player

    while any(enemy.is_alive() for enemy in enemies) and player.is_alive():

        enemy = random.choice([e for e in enemies if (e.is_alive() and e != current_player)])
        print (enemy.name)

        print(f"{player.name} (HP: {player.hp}) vs. {enemy.name} (HP: {enemy.hp})")
        print("What will you do?")
        choice = input("(A)ttack or use (S)pecial move: ").strip().lower()

        if choice == 'a':
            current_player.attack(enemy)
        elif choice == 's' and isinstance(current_player, Mage):
            current_player.cast_spell(enemy)
        elif choice == 's' and isinstance(current_player, Warrior):
            current_player.defend(enemy)
        elif choice == 's' and isinstance(current_player, Rogue):
            current_player.Critical_hit(enemy)
            
        else:
            print("Invalid choice. Try again.")
        

        current_player, enemy = enemy, current_player

        for enemy in enemies:
            if enemy.is_alive() and player.is_alive():
                enemy_choice = random.choice(['a', 's'])
                if enemy_choice == 'a':
                    current_player.attack(player)
                elif enemy_choice == 's' and isinstance(enemy, Mage):
                    enemy.cast_spell(player)
                elif enemy_choice == 's' and isinstance(enemy, Warrior):
                    enemy.defend(enemy)
                elif enemy_choice == 's' and isinstance(enemy, Rogue):
                    enemy.Critical_hit(player)
                    
        continue  
    print("Game over!")
    if player.is_alive():
                  print(f"{player.name} wins!")
    else:
                  print("Enemies win!")

main()
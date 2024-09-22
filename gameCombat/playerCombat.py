class Character:
    def __init__(self, name, in_max_hp, in_max_mp, inventory, armor_class, level):
        self.name = name
        self.max_hp = in_max_hp  
        self.max_mp = in_max_mp  
        self.hp = in_max_hp  # set the internal hp and mp to the max
        self.mp = in_max_mp  # Corrected attribute name
        self.inventory = inventory
        self.armor_class = armor_class
        self.level = level

    def display_info(self):
        """
        Displays character information.
        """
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}/{self.max_hp}") 
        print(f"MP: {self.mp}/{self.max_mp}")  
        print(f"Armor Class: {self.armor_class}")
        print(f"Level: {self.level}")

# Example usage:
hero = Character(name="Sir Lancelot", in_max_hp=100, in_max_mp=50, inventory={"gold": 10, "torch": 1}, armor_class=15, level=1)
hero.display_info()

class Player(Character):
    def __init__(self, name, in_max_hp, in_max_mp, inventory, armor_class, level):
        super().__init__(name, in_max_hp, in_max_mp, inventory, armor_class, level)
        self.exp = 0
        self.LEVEL_UP = 100  # Adjust as needed for leveling up

    def level_up(self):
        """
        Handles character leveling up.
        """
        if self.exp >= self.LEVEL_UP:
            # Implement attribute point allocation here
            # Example: self.ATTRIBUTES['strength'] += 1
            # Update max_hp and max_mp based on level
            return True
        else:
            return False

    def gain_exp(self, exp):
        """
        Adds experience points to the character.
        """
        self.exp += exp
        print(f"You gained {exp} XP")
        if self.level_up():
            print(f"Congratulations, you gained a level!\nYour current level is {self.level}\n")
        else:
            print(f"Your current XP is {self.exp}/{self.LEVEL_UP}")

    def attack(self, target):
        """
        Simulates an attack on the target.
        """
        damage = 10  # Placeholder for damage calculation (customize as needed)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.hp <= 0:
            print(f"{target.name} has been defeated!")

# Example usage:
hero = Player(name="Sir Lancelot", in_max_hp=100, in_max_mp=50, inventory={"gold": 10, "torch": 1}, armor_class=15, level=1)
enemy = Character(name="Evil Goblin", in_max_hp=50, in_max_mp=0, inventory={}, armor_class=12, level=1)

hero.attack(enemy)
enemy.display_info()

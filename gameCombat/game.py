class Character:
    def __init__(self, name, max_hp, max_mp, inventory, armor_class, level):
        self.name = name
        self.max_hp = max_hp  
        self.max_mp = max_mp  
        self.hp = max_hp  # set the internal hp and mp to the max
        self.mp = max_mp  # Corrected attribute name
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
hero = Character(name="Sir Lancelot", max_hp=100, max_mp=50, inventory={"gold": 10, "torch": 1}, armor_class=15, level=1)
hero.display_info()


class Player(Character):
    ATTRIBUTES = {'strength': 0, 'constitution': 0, 'dexterity': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}
    EQUIPMENT_SLOTS = {'head': None, 'chest': None, 'legs': None, 'boots': None}

    def __init__(self, armor_class):
        super().__init__(input("Tell us your name, hero:\n> "), 20, 10, {'gold': 10, 'torch': 1}, armor_class, 1)
        self.exp = 0
        self.max_hp = self.hp
        self.max_mp = self.mp
        self.LEVEL_UP = 500

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

# Example usage:
player = Player(armor_class=18)
player.gain_exp(50)

## Game Characters and Abilities Example

### 1. Character Class


class Character:
    def __init__(self, name, max_hp_in, max_mp_in, inventory, armor_class, level):
        self.name = name
        self.hp = max_hp_in
        self.mp = max_mp_in
        self.max_hp = max_hp_in
        self.max_mp = max_hp_in
        self.inventory = inventory
        self.armor_class = armor_class
        self.level = level
        self.LEVEL_UP = 500
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
hero = Character(name="Sir Lancelot", max_hp_in=100, max_mp_in=50, inventory={"gold": 10, "torch": 1}, armor_class=15, level=1)
hero.display_info()


### 2. Attributes and Equipment Slots


class Player(Character):
    ATTRIBUTES = {'strength': 0, 'constitution': 0, 'dexterity': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}
    EQUIPMENT_SLOTS = {'head': None, 'chest': None, 'legs': None, 'boots': None}

    def __init__(self, armor_class):
        super().__init__(input("Tell us your name, hero:\n> "), 20, 10, {'gold': 10, 'torch': 1}, armor_class, 1)
        self.exp = 0
        self.max_hp = self.hp
        self.max_mp = self.mp

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

# Example usage:
player = Player(armor_class=18)
player.gain_exp(50)

# Define the Animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        """
        Simulates the animal's sound.
        Modify this method to customize sounds for different animals.
        """
        return f"{self.name} says woof!"

#question?  Can we use this for anything yet right now?
# or is this just the 'blueprint'?
#
#what do we need to do to 'use' this blueprint?

# Investigate: Explore attributes and methods
# 1. Create additional animal instances
cat = Animal(name="Whiskers", species="Cat")
bird = Animal(name="Tweety", species="Bird")

print(f"{cat.name} is a {cat.species}")
print(f"{bird.name} is a {bird.species}")
cat = Animal(name="Tabby", species="Cat")
dog = Animal(name="Contora", species="Dog")

#question?  How many instances of the animal class have we created to this point?


class Bird(Animal):
    def fly(self):
        """
        Simulates the bird's flying behavior.
        """
        return f"{self.name} gracefully takes flight."
    def speak(self):
        """
        Simulates the animal's sound.
        Modify this method to customize sounds for different animals.
        """
        return f"{self.name} says tweet tweet tweet!"

# Create a bird instance
parrot = Bird(name="Polly", species="Parrot")
print(parrot.fly())
print(parrot.speak())
#what's going on here?  Is this an Animal class?  A bird class?
#can it be both?
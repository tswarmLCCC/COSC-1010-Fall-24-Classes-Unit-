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

# Example usage:
dog = Animal(name="Buddy", species="Dog")
print(dog.speak())

# Investigate: Explore attributes and methods
# 1. Create additional animal instances
cat = Animal(name="Whiskers", species="Cat")
bird = Animal(name="Tweety", species="Bird")

# 2. Print details of each animal
print(f"{cat.name} is a {cat.species}")
print(f"{bird.name} is a {bird.species}")

# Modify: Enhance attributes and extend behavior
# Add two new animals types, create one of each (make an instance), and run thier
# 'movement' menthod
class Bird(Animal):
    def fly(self):
        """
        Simulates the bird's flying behavior.
        """
        return f"{self.name} gracefully takes flight."

# Create a bird instance
parrot = Bird(name="Polly", species="Parrot")
print(parrot.fly())

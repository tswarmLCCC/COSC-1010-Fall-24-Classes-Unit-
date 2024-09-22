# Define the Animal class
class Animal:
    def __init__(self, in_name, in_species):
        self.name = in_name
        self.species = in_species

    def speak(self):
        """
        Simulates the animal's sound.
        Modify this method to customize sounds for different animals.
        """
        return f"{self.name} says woof!"

# Example usage:
dog = Animal(in_name="Buddy", in_species="Dog")
print(dog.speak())
print(dog.name)
print(dog.species)

cat = Animal(in_name="Tabby", in_species="Cat")
print(cat.speak())
print(cat.name)
print(cat.species)


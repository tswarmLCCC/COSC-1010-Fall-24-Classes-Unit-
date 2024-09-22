# Define the Animal class
class Animal:
    def __init__(self, in_name, in_species):
        self.name = in_name
        self.species = in_species
        self.age = 0
        self.__furcolor = "Brown"

    def getFurColor(self):
        return self.__furcolor

    def setname(self, in_name):
        self.name = in_name

    def setAge(self, in_age):
        if int(in_age) < 0 :
            print("Please only use positive values")
        self.age = in_age

    def getname(self):
        return(self.name)

    def speak(self):
        """
        Simulates the animal's sound.
        Modify this method to customize sounds for different animals.
        """
        return f"{self.name} says woof!"

# Example usage:
dog = Animal(in_name="Buddy", in_species="Dog")
print(dog.getFurColor())

##print(dog.__furcolor)
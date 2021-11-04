class Dog():
    """
    A class to represent a general dog
    """

    def __init__(self, name, gender, age):
        """
        Initialise attributes
        """
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        """Feed the dog"""
        if self.gender == "male":
            print("Here " + self.name + "! Good boy! Eat up.")
        else:
            print("Here " + self.name + "! Good girl! Eat up.")

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print("WOOF WOOF WOOF WOOF WOOF")
        else:
            print("woof...")
    
    def compute_age(self):
        """Compute the age in dog years"""
        dog_years = self.age*7
        print(self.name + " is " + str(dog_years) + " years old in dog years.")


class Beagle(Dog):
    """A class to represent a specific type of dog"""

    def __init__(self, name, gender, age, is_gun_shy):
        # Call the initialisation of the super (parent) class
        super().__init__(name, gender,age)
        self.is_gun_shy = is_gun_shy

    def hunt(self):
        """If the dog is not gun shit, take them hunting"""
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + " just brought back a duck")
        else:
            print(self.name + " is not a good hunting dog")

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print("HOWL HOWL HOWL")
        else:
            print("howl")
    

beagle = Beagle("kady", "female", 10, False)
beagle.eat()
beagle.bark(False)
beagle.compute_age()
beagle.hunt()

# The dog class can't hunt!
dog = Dog("Spotty dog", "male", 3)
# dog.hunt()
dog.bark(True)
beagle.bark(True)

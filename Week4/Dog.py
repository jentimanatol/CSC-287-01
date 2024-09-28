#-------------------------------------------------------------
class Dog:
    """A simple attempt to model a dog.""" #camel casses = 3 doublescoor

    def __init__(self, name, age):    #class sonstructor -> an instance metod 
        """Initialize name and age attributes."""   #self is a reference to the object Itselph 
        self.name = name                     #initialise instance variable
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#--------------------------------------------------------------

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
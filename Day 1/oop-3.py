class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        print(f"{self.name} say MOOOO!")

class Cat(Pet):
    def __init__(self, name, age, color):
        # used to call the parent class we're using to pass into the parents __init__ where other methods/things may happen
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print(f"{self.name} says Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and {self.color}.")
        
class Dog(Pet):
    def speak(self):
        print(f"{self.name} says Woof")
        
class Fish(Pet):
    pass
        
p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Bill", 34, "Blue")
c.show()
c.speak()
d = Dog("Frank", 16)
d.show()
d.speak()
f = Fish("Jill", 15)
f.speak()

string = "hello"
#.upper is a method
# print(string.upper())
# this will print HELLO in the console


# defing a new class with the name Dog
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    # creating a method on the class Dog for barking
    def bark(self):
        # this will print bark in the console
        print("bark")
        
    def meow(self):
        # you don't have to print, you could return something
        return "meow"
    
    def add_one(self, x):
        # add one to whatever we pass in for x
        return x + 1
    
    
        
# assign the variable d to an instance of our Dog Class
dog1 = Dog("Stanley", 12)
dog2 = Dog("Leroy", 5)
# using our bark method on our variable d
# dog1.bark()
# using our meow method
# print(dog1.meow())
# using our add_one method
# print(dog1.add_one(5))
# printing the type of d to show its a class of __main__.Dog
# print(type(d))     


# calling on our instance of dog and its .name directly
# print("The first dog is:")
# print(dog1.name)
# print("The second dog is:")
# print(dog2.name)

# this is after setting up the method get_name and get_age
print("The first dog is:")
print(dog1.get_name())
print("Age is:")
print(dog1.get_age())
print("The second dog is:")
print(dog2.get_name())
print("Age is:")
print(dog2.get_age())

dog1.set_age(44)
print("The first dogs age is now:")
print(dog1.get_age())


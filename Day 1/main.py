
string = "hello"
#.upper is a method
print(string.upper())
# this will print HELLO in the console


# defing a new class with the name Dog
class Dog:
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
d = Dog()
# using our bark method on our variable d
d.bark()
# using our meow method
print(d.meow())
# using our add_one method
print(d.add_one(5))


#printing the type of d to show its a class of __main__.Dog
print(type(d))        
from turtle import Turtle

# Class Inheritance
class Snake(Turtle): # class snake is the inheritance from the turtle class
    def __init__(self):
        super().__init__() # snake class is inherit all the attributes and methods from the turtle class
        self.shape("circle")
        # etc.

# Slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# Slicing list
print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])

# Slicing tuple
print(piano_tuple[2:5])
print(piano_tuple[2:])
print(piano_tuple[2:5:2])
print(piano_tuple[::2])
print(piano_tuple[::-1])
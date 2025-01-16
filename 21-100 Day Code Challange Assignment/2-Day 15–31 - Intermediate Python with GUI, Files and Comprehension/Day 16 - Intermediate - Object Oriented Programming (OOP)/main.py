"""Constructing Objects and Accessing their Attributes and Methods"""

from turtle import Screen, Turtle

# Create an Object
timmy = Turtle()
print(timmy)  # output: <<module>.<Class> object at <memory_location>>
timmy.shape("turtle")  # change the shape of object
timmy.color("coral")  # change the color
timmy.forward(100)  # move 100

# Object Attributes
my_screen = Screen()
print(my_screen.canvheight)  # <object>.<attribute>

# Object Methods
my_screen.exitonclick()  # <object>.<method>


# Create an Object from PrettyTable Class
from prettytable import PrettyTable  # Install external package  # noqa: E402

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # Change the Object Attribute
print(table)

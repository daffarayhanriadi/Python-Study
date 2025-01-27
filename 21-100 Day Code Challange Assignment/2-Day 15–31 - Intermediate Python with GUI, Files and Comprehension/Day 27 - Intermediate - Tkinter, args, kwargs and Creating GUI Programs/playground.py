# Challenge-1:
"""
Modify the add function to take an unlimited number of arguments. 
Use a loop to sum all the arguments inside the function.
Test it out by calling add() to calculate sum of some arguments.
"""

# *args
# def add(*args):
#     print(args)
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1,2,3,4,5,6,7,8,9,10))

# **kwargs
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs:
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)


# Create a Class with **kwargs like Tkinter Module's Class
class Car:
    def __init__(self, **kw):
        # self.make = kw["make"] # If kw value doesn't exist, the code will be error when run it.
        self.make = kw.get("make")  # If kw value doesn't exist, the code will return None and the code will not error.
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)  # Return Nissan
print(my_car.model)  # Return Skyline
print(my_car.colour)  # return None
print(my_car.seats)  # return None

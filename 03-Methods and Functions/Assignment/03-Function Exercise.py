"""Function Exercise"""

import os
from typing import Union

# Program for calculating the area and perimeter of rectangles

# # Making program header
# os.system("cls")

# print(f"{'AREA CALCULATION PROGRAM':^40}")
# print(f"{'AND PERIMETER OF RECTANGLE':^40}")
# print(f"{'-'*40:^40}")

# # Retrieve user input
# WIDTH = int(input("Insert width value: "))
# LENGTH = int(input("Insert length value: "))

# # Area calculation program
# AREA = LENGTH * WIDTH
# PERIMETER = 2 * (LENGTH + WIDTH)

# # Display the result
# print(f"Area calculation result = {AREA}")
# print(f"Perimeter calculation result = {PERIMETER}")

def header() -> None:
    """Header function"""
    os.system("cls")
    print(f"{'AREA CALCULATION PROGRAM':^40}")
    print(f"{'AND PERIMETER OF RECTANGLE':^40}")
    print(f"{'-'*40:^40}")
    
def input_user() -> tuple[int, int]:
    """Input User function"""
    width = int(input("Insert width value: "))
    length = int(input("Insert length value: "))
    
    return width, length

def area_calculation(width: Union[int, float], length: Union[int, float]) -> Union[int, float]:
    """Area function"""
    return width * length

def perimeter_calculation(width: Union[int, float], length: Union[int, float]) -> Union[int, float]:
    """Perimeter function"""
    return 2 * (width + length)

def display(message: str, value: Union[int, float]) -> None:
    print(f"{message} calculation result = {value}")

# Main program
while True:
    header()
    
    WIDTH, LENGTH = input_user()
    AREA = area_calculation(WIDTH, LENGTH)
    PERIMETER = perimeter_calculation(WIDTH, LENGTH)
    
    display("Area", AREA)
    display("Perimeter", PERIMETER)
        
    isContinue: str = input("Is it continue (y/n)? ")
    if isContinue[0].lower() == "n":
        break

print("Program completed, thank you")
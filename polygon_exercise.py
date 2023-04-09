# Name: Claudio Fischer
# UNumber - U92525778
'''
Description:
This Python program defines a class called "Polygon" that represents a 
regular polygon with a given number of sides and side length. The class has 
methods to get and change the number of sides and side length, and to 
calculate the perimeter and area of the polygon.

The program also has a main function that creates an instance of the Polygon class, 
prompts the user to enter the number of sides and length of the polygon, 
validates the input, and then uses the methods of the Polygon class to calculate 
and display the perimeter and area of the polygon.
'''

import math

class Polygon:
    def __init__(self):
        self.__sides = 0
        self.__length = 0.00

    def num_sides(self):
        return self.__sides

    def num_length(self):
        return self.__length

    def change_sides(self, updated_side):
        self.__sides = updated_side

    def change_length(self, updated_length):
        self.__length = updated_length

    #calculate the perimeter of the polygon
    def perimeter(self):
        return self.__length * self.__sides

    #calculate the area of the polygon
    def area(self):
        return (self.__sides * (self.__length ** 2)) / (4 * math.tan(math.pi / self.__sides))


def main():
    polygon1 = Polygon()
    sides = int(input("Enter the number of sides (>=3): "))

    while sides < 3:
        sides = int(input("Invalid entry. Re-enter the number of sides (>=3): "))
    length = float(input("Enter the length of each sides (>= 0.1): "))

    while length < 0.1:
        length = float(input("Invalid entry. Re-enter the length of each sides (>= 0.1): "))
    polygon1.change_sides(sides)
    polygon1.change_length(length)
    print(f"The polygon has {polygon1.num_sides()} sides. Each side is {polygon1.num_length()} units in length.")
    print(f"The perimeter of the polygon is {polygon1.perimeter():.3f} units and its area is {polygon1.area():.3f} square units.")


#--- call main function() ---
main()




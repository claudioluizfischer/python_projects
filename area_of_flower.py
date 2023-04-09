'''
Name: Claudio Fischer
Unumber: 92525778
Description: This program calculates the area of a flower composed by 
the area of a square and four semi circles. The program allows the user
to input the radius of the flower and uses this number to calculate the total 
area through using three formulas developed along the code.
'''

#pi stores a value to be used later in the code
pi = 3.14159

flower_radius = float(input("Enter the radius of the flower:"))

square_area = ((flower_radius / 2) * 2) ** 2

semi_circle_radius = (pi * (flower_radius/2) ** 2) / 2

total_flower_area = square_area + (4 * semi_circle_radius)

print(f"The area of the flower is {total_flower_area} square units.")
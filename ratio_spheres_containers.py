'''
Name: Claudio Fischer
Unumber: 92525778
Description: This program proves that the volume of any sphere is 2/3 of the volume of any cylinder with
equivalent radius and height equal to the diameter. Initially, the program asks for the number of
spheres and the diameter of each sphere. Then calculates the height of the container and the volume
occupied by the spheres in the container.
'''

#Using math module to use the value of pi later in the code
import math

number_spheres = int(input("Enter the number of spheres to be placed in the container:"))

diameter_sphere = float(input("Enter the diameter of each sphere (in inches):"))

sphere_radius = diameter_sphere / 2

#Using math module's version of pi
sphere_volume = (4 * math.pi * (sphere_radius ** 3)) / 3

cylinder_volume = math.pi * (sphere_radius ** 2) * (3 * diameter_sphere)

height_required = number_spheres * diameter_sphere

print(f"The container would need to be at least {height_required} inches to hold the {number_spheres} spheres.")

required_occupancy = (number_spheres * sphere_volume) / cylinder_volume

#Using appropriate percent formatting to express the volume occupied by the spheres inside the cylinder
print(f"The {number_spheres} spheres will occupy {required_occupancy:.2%} of the container.")
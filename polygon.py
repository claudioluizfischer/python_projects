'''
Claudio Fischer
U92525778
Description: Program that drwas a polygon according to user's input such as
number of sides and the lentgh of each side. In this program, I used the turtle's
method to read the user's input and to draw the polygon.
'''

import turtle

number_sides = int(turtle.numinput('Numerical Input Box', 'Enter number of sides:', default = 3, minval = 3, maxval = 12))
lenght_sides = int(turtle.numinput('Numerical Input Box', 'Enter the length of each side:', default = 50, minval = 50, maxval = 250))

#Calculate the angle between each side
angle = (180*(number_sides - 2))/ number_sides

#turn_angle determs at which angle should the turtle turn
turn_angle = 180 - angle

#loop for drawing the polygon
for side in range(number_sides):
    turtle.color('green') #exploring the methods, this is to make the turtle green
    turtle.pensize(5) # just exploring the methods, this is to increase the the size of the turtle's displacement
    turtle.forward(lenght_sides)
    turtle.right(turn_angle)

# if elif statements for displaying the polygon's names in the graphics window according to their number of sides
if number_sides == 1:
    turtle.write("Monogon")
elif number_sides == 2:
    turtle.write("Digon")
elif number_sides == 3:
    turtle.write("Triangle")
elif number_sides == 4:
    turtle.write("Quadrilateral")
elif number_sides == 5:
    turtle.write("Pentagon")
elif number_sides == 6:
    turtle.write("Hexagon")
elif number_sides == 7:
    turtle.write("Heptagon")
elif number_sides == 8:
    turtle.write("Octagon")
elif number_sides == 9:
    turtle.write("Nonagon")
elif number_sides == 10:
    turtle.write("Decagon")
elif number_sides == 11:
    turtle.write("Hendecagon")
elif number_sides == 12:
    turtle.write("Dodecagon")
    
turtle.Screen().exitonclick()
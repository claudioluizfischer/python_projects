'''
Name: Claudio Fischer
Unumber: 92525778
Description: This program calculates and outputs the coordinates of the two points
and the slope of a line that connects them. Through the user's input (coordinates
of the first point and the coordinates of the second point), the program
uses the slope formula to calculate the slope of a line.
'''

#Here, the split() function had to be used in order to allow the user to input two coordinates at the same time by using the space of the keyboard.
x1, y1 = input("Enter the coordinates of the first point:").split()

x2, y2 = input("Enter the coordinates of the second point:").split()

#The strings x1, y1 and x2,y2 had to be transformed as float numbers to calculate the slope;therefore, the slope is also a number
slope = (float(y2) - float(y1)) / (float(x2) - float(x1))

print(F"The slope of the line that connects two points ({x1},{y1}) and ({x2}, {y2}) is {slope:.3f}")
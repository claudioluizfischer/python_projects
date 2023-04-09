'''
Name: Claudio Fischer
U2525778
Description: Restaurant Selector -> This program inputs various dietary information
from your friends and according to how the inputs are assigned, it outputs the restaurants
in which you would be able to take all of your friends.
'''

vegetarian = input("Is anyone in your party a vegetarian? ").lower()

vegan = input("Is anyone in your party a vegan? ").lower()

gluten_free = input("Is anyone in your party gluten free? ").lower()

print("Here are your restaurant choices:")

if vegetarian == 'no':
  if vegan == 'no':
    if gluten_free == 'no':
      print("Fleming's Prime Steakhouse")
if vegan == 'no':
  print("Gourmet Pizza Company")
  if gluten_free == 'no':
    print("Bella's Italian Restaurant")

print("True Food Kitchen")
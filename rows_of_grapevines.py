'''
Name: Claudio Fischer
Unumber: 92525778
Description: This program asks the user for two inputs (length of row and amount of space used by an
end-post assembly) and uses these inputs to calculate and display the number of grapevines that
will fit in the especific row assigned by the especifications of the user. 
'''

length_row = int(input("Enter the length of the row, in feet:"))

end_pot_assembly_space = float(input("Enter the amount of space, in feet, used by an end-post assembly:"))

distance_between_vines = int(input("Enter the distance, in feet, between each vine:"))

numbers_of_vines = (length_row - (2 * (end_pot_assembly_space))) / distance_between_vines

print(F"You have enough space for {numbers_of_vines} vines.")
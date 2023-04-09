'''
Name: Claudio Fischer
Unumber: U92525778
Description: This program quizzes the users on their knowledge of state capitals.
By randomly displaying the name of a state and asking the user to enter the
state's capital, this program uses a dictionary called state_capitals that
contains the names of all the US states and their corresponding capitals.
The dictionary is converted into a list by using the list() function.
A while loop checks the user's answers while counting the number of correct and
incorrect responses and stopping the game when the user enter 'q'. 
'''

import random

# Define a dictionary of states and their capitals
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Convert the dictionary to a list in order to retrieve indices
state_list = list(state_capitals.keys())

#Initialize counters for correct and incorrect answers
num_correct = 0
num_incorrect = 0

state = random.choice(state_list) # Randomly select a state from the list usign the module random with the choice function
answer = input(f"What is the capital of {state}? (or enter q to quit): ")

while answer != "q":
    # Check if the user's answer is correct
    if answer.lower() == state_capitals[state].lower():
        print("That is correct.")
        num_correct += 1
    else:
        print(f"That is incorrect.")
        num_incorrect += 1

    state = random.choice(state_list)
    answer = input(f"What is the capital of {state}? (or enter q to quit): ")

# Print the final results
print(f"You had {num_correct} corerct responses and {num_incorrect} incorrect responses.")
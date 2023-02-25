'''
Claudio Fischer
U92525778
Description: This is a interactive guessing game. The program randomly generates a number between
1 and 100, including 1 and 100. The user has up to 10 tires to guess the number. If the user uses all
the available guesses and still does not get the number correct, the program outputa a message saying 
the correct number and it stops. The program ensures that every guess is within the correct range.
It uses a while loop to keep the user guessing if they haven't guessed the right number and they haven't
used all their tires. When the user correctly guesses the number (without using all their tries), the loop
ends.
'''

import random as rn

# r is the range -> 1 to 100
r = rn.randint(1,100)

# Variable to count the number of guesses
count = 0

num = int(input("Enter a number between 1 and 100 (inclusive): "))
if num < 0 or num > 100:
    while num < 0 or num > 100:
        num = int(input("Really? Enter another guess between 1 to 100 (inclusive): "))
else:
    while (num != r):
        if num > 0 and num <= 100:
            count = count + 1
            if count >= 10:
                print(f"Sorry, the number was {r}")
                break
            else:
                if num > r:
                    num = int(input("Too high. Enter another guess: "))
                elif num < r:
                     num = int(input("Too low. Enter another guess:"))
                else: #when the player get the number correctly
                    print(f"You guessed it right!! You got it in {count} guesses!")
        else:
            num = int(input("Really? Enter another guess between 1 to 100 (inclusive): "))
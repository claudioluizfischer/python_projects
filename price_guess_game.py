'''
Name: Claudio Fischer
U92525778
Description: The Price is Right! (One Bid) -> The program simulates one bit in the game
of the game show that focuses on players correclty predicting prices of items for cash and
prizes. The program generates a random numbers between 1000 and 5000 and
it inputs the bits from 4 players. Then it determs if the bids are greater than the actual
price. If all of the bids are greater than the actual price, the programs outputs
a message letting everyone know that the everyone has overbid and it finishes running. 
Otherwise, if one of the bids is ecxatly the same as the actual price, the program outputs
a different message showing which player guesssed correctly. If this is not the case, the
propgram compares what is the closest bid form each player and outputs a message describing who won.
The bid that is greater than the actual price is not compared. However, the bid that gets closer to 
the actual price and is less than the actual price wins.
'''

import math
import random as rn

# r is the range of price -> $1000 to $5000
r = rn.randint(1000, 5000)

num1 = int(input("Player 1, what is your bid? "))
num2 = int(input("Player 2, what is your bid? "))
num3 = int(input("Player 3, what is your bid? "))
num4 = int(input("Player 4, what is your bid? "))

'''
if the difference number calculated is less than the random number generated,
the new number from each particular partcipant is assigned the number of r.
'''
new_num1 = r - num1
if new_num1 < 0:
  new_num1 = r
new_num2 = r - num2
if new_num2 < 0:
  new_num2 = r
new_num3 = r - num3
if new_num3 < 0:
  new_num3 = r
new_num4 = r - num4
if new_num4 < 0:
  new_num4 = r

#variable n determs the index of the player that satisfy the condition
if num1 > r and num2 > r and num3 > r and num4 > r:
  print("Buzz!Aww...everyone has overbid!")
elif num1 == r or num2 == r or num3 == r or num4 == r:
  if num1 == r:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${r}! Player 1, come on up!")
  if num2 == r:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${r}! Player 2, come on up!")
  if num3 == r:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${r}! Player 3, come on up!")
  if num4 == r:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${r}! Player 4, come on up!")
else:
  if new_num1 < new_num2 and new_num1 < new_num3 and new_num1 < new_num4 and new_num1 > 0:
    print(f"Actual price is ${r}! Player 1, come on up!")
  if new_num2 < new_num1 and new_num2 < new_num3 and new_num2 < new_num4 and new_num2 > 0:
    print(f"Actual price is ${r}! Player 2, come on up!")
  if new_num3 < new_num1 and new_num3 < new_num2 and new_num3 < new_num4 and new_num3 > 0:
    print(f"Actual price is ${r}! Player 3, come on up!")
  if new_num4 < new_num1 and new_num4 < new_num2 and new_num4 < new_num3 and new_num4 > 0:
    print(f"Actual price is ${r}! Player 4, come on up!")
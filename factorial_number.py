'''
Claudio Fischer
U92525778
Description: This program allows the user to enter a positive number
through a while loop which validates the input value to be a non-negative number.
Then, it uses a loop to calculate the factorial of that number.
'''
n = int(input('Enter a nonnegative number:'))
while n < 0:
    n = int(input('Enter a nonnegative number:'))

#total variable stores the factorial value for each loop
total = 1
for i in range (1, n + 1):
    total = total * i

print(f'The factorial of {n} is {total:,}')



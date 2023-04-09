#This program prompts the user for a numerator and a denominator. It then determines
#if the fraction is proper or improper, it it can be reduced using the gcd, and if improper,
#converts it to a mixed number.

from math import gcd
#get numerator and denominator (and also validate input)
number = int(input('Enter a numerator: Value must be greater than 0: '))
while number <= 0:
  number = int(input('Please re-enter the numerator. Value must be greater than 0: '))

denom = int(input('Enter a denominator. Value must be greater than 0:'))
while denom <=0:
  denom = int(input('Please re-enter the denominator. Value must be greater than 0:'))

#calculate greatest common divisor
factor = gcd(number, denom)

#determine proper or improper fraction (and reduce if possible)
if number < denom:
# it is a proper fraction
  print(f'{number} / {denom} is a proper fraction.')

  #check for reduction
  if (factor == 1):
    print('This proper fraction cannot be reduced any further.')
  else:
    print(f'This proper fraction can be reduced to: {number // factor} / {denom / factor}')

#otherwise, the fraction is improper
else:
  print(f'{number} / {denom} is an improper fraction.')

#check for reduction
  if (factor == 1):
    print('This improper fraction cannot be reduced any further.')

    #calculate mixed number (if values can't be reduced)
    wholenum = number / denom
    frac = number % denom
    if frac == 0:
      print(f'The whole number is {number // denom}')
    else:
      print(f'The mixed number is {number // denom} and {number % denom} / {denom}')

  else:
    n2 = number / factor
    d2= denom / factor
    print(f'This improper fraction can be reduced to {n2} / {d2}')

    #calculate mixed number (with reduced values)
    wholenum = n2 / d2
    frac = n2 % d2
    if frac == 0:
      print(f'The whole number is {n2 / d2}')
    else:
      print(f'The mixed number is {n2 / d2} and {n2 % d2}')

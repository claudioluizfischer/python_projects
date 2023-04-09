'''
Claudio FIscher
U92525778
Description: This program inputs 2 numbers from the user. It verifies if the relation to the numerador and denominator are
outputs a proper or improper fraction. If it is proper and can be reduced, it reduces the inputed numbers and outputs
the integer number if generated. The program also verifies if the user is inputing numbers greater than 0 and if not it
asks the user to re-enter inputs accordingly.
'''

import math

numerator = int(input("Enter a numerator: Value must be greater than 0:"))
if numerator > 0:
    denominator = int(input("Enter a denominator: Value must be greater than 0:"))
    if denominator > 0:
        if (numerator % 2 == 0) and (denominator % 2 == 0):
            new_numerator = numerator / 2
            new_denominator = denominator / 2
        elif (numerator % 3 == 0) and (denominator % 3 == 0):
            new_numerator = numerator / 3
            new_denominator = denominator /3

        if numerator < denominator:
            print(f"{numerator} / {denominator} is a proper fraction.")
            print(f"This proper fraction can be reduced to {new_numerator} / {new_denominator}")
        if (numerator % 2 == 0) and (denominator % 2 == 0):
            new_numerator = numerator / 2
            new_denominator = denominator / 2
        elif (numerator % 3 == 0) and (denominator % 3 == 0):
            new_numerator = numerator / 3
            new_denominator = denominator /3
        elif numerator > denominator:
            print(f"{numerator} / {denominator} is an improper fraction.")
            print(f"This improper fraction cannot be reduced any further.")
        elif new_denominator == 1:
            print(f"The whole number is {new_numerator}")
    else:
        denominador = int(input("Please re-enter the denominator. Value must be greater than 0:"))
        if (numerator % 2 == 0) and (denominator % 2 == 0):
            new_numerator = numerator / 2
            new_denominator = denominator / 2
        elif (numerator % 3 == 0) and (denominator % 3 == 0):
            new_numerator = numerator / 3
            new_denominator = denominator /3

        if numerator < denominator:
            print(f"{numerator} / {denominator} is a proper fraction.")
            print(f"This proper fraction can be reduced to {new_numerator} / {new_denominator}")
            mix_number = math.gcd(numerator, denominator)
            print(f"The mixed number is {mix_number} and {numerator} / {denominator}")
        elif numerator > denominator:
            print(f"{numerator} / {denominator} is an improper fraction.")
            print(f"This improper fraction cannot be reduced any further.")
            mix_number = math.gcd(numerator, denominator)
            print(f"The mixed number is {mix_number} and {numerator} / {denominator}")
else:
    numerator = int(input("Please re-enter the numerator. Value must be greater than 0:"))
    denominator = int(input("Enter a denominator: Value must be greater than 0:"))
    if (numerator % 2 == 0) and (denominator % 2 == 0):
        new_numerator = numerator / 2
        new_denominator = denominator / 2
    elif (numerator % 3 == 0) and (denominator % 3 == 0):
        new_numerator = numerator / 3
        new_denominator = denominator /3

    if numerator < denominator:
        print(f"{numerator} / {denominator} is a proper fraction.")
        print(f"This proper fraction can be reduced to {new_numerator} / {new_denominator}")
        mix_number = math.gcd(numerator, denominator)
        print(f"The mixed number is {mix_number} and {numerator} / {denominator}")
    elif numerator > denominator:
        print(f"{numerator} / {denominator} is an improper fraction.")
        print(f"This improper fraction cannot be reduced any further.")
        mix_number = math.gcd(numerator, denominator)
        print(f"The mixed number is {mix_number} and {numerator} / {denominator}")

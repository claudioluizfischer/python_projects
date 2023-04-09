'''
Name: Claudio Fischer
U92525778
Description: This programs uses a recursion function to raise a number to a power given through
user's input. The function uses two arguments and the function power returns the result if the exponent
provided is not 0. In the main() function, the program also uses input validation to ensure that
the exponent is between the correct range.
'''
def main():
    base = int(input("Enter a base: "))
    if base <= 0:
        return main() #calls the function again so that the user has the chance to input a valid base number  
    whole_number = int(input("Enter a whole number between 2 and 50: "))
    if whole_number < 2 or whole_number > 50:
        whole_number = int(input("Invalid. Please enter a whole number between 2 and 50: "))
    print(f"{base} to the power of {whole_number} is {power(base,whole_number)}") #calls function power()


def power(base, whole_number):
    if whole_number == 0: #every number raised to the 0 power equals one
        return 1
    else:
        return (base * power(base, whole_number - 1))

#---- calling main function -------
main()

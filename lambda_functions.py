'''
Claudio Fischer
U92525778
Description: This program is made of two functions that together mimic the basic 
mathematical operations. The main() function inputs the operation, numbers to be considered
and calls the math_operation() function where it contains the basic functions, and
inside this function the lambda function is used to calculate the operation inside an if elif else
structure.
'''

def main():
    while True:
        try:
            operation = input("Enter the operation as a symbol (e.g. + for addition): ")
            number_1, number_2 = input("Enter two values, separated by a space: ").split()
            num1 = float(number_1)
            num2 = float(number_2)
            print(math_operation(operation, num1, num2)(num1, num2))
        except TypeError:
            break

def math_operation(operation, num1, num2):
        if operation == '+': #addition
            return lambda x, y: x + y #the following line passes the num1 and num2 as arguments x and y to this lambda function
        elif operation == '-': #subtraction
            return lambda x, y: x - y
        elif operation == '*': #multiplication
            return lambda x, y: x * y
        elif operation == '/': #floating point division
            return lambda x, y: x / y
        elif operation == '//': #integer division
            return lambda x, y: x // y
        elif operation == '%': #modulus operator
            return lambda x, y: x % y
        elif operation == '**': #exponent
            return lambda x, y: x ** y
        else: #if the user inputs an math function different from the ones above
            invalid_result = lambda: print(f"{num1} {operation} {num2} = Invalid operation")
            return invalid_result()
        
    

#calling main function
main()
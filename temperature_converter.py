#Claudio Fischer
#U92525778
'''
Description: This program converts the temperature inputed by a user by calling function which
contain formulae that return the converted values accordingly. 
'''

def main():
    options()
    number_chosen = int(input("Please select an option: "))
    while number_chosen <= 0 or number_chosen >= 7:
        number_chosen = int(input("Invalid choice. Please re-select an option: "))
    temp = float(input("Enter a temperature: "))

    choices_dict = {1: celsius_to_fahrenheit(temp), 
                    2: celsius_to_kelvin(temp), 
                    3: fahrenheit_to_celsius(temp), 
                    4: fahrenheit_to_kelvin(temp), 
                    5: kelvin_to_celsius(temp),
                    6: kelvin_to_fahrenheit(temp)
                    }
    
#I didn't do this part on time
    if number_chosen == 1:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    elif number_chosen == 2:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    elif number_chosen == 3:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    elif number_chosen == 4:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    elif number_chosen == 5:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    elif number_chosen == 6:
        print(f"{temp} degrees Celsius is {choices_dict[number_chosen]:.2f} degrees Fahrenheit.\n")
    else:
        pass

    convert_again = input("Would you like to convert another temperature? ")
    while True:
        if convert_again.lower() == "no":
            break
        else:
            main()

def options():
    print("This program will convert temperatures for you!")
    print("Here are the options:")
    print("1. Convert from Celsius to Fahrenheit\n" +
      "2. Convert from Celsius to Kelvin\n" +
      "3. Convert from Fahrenheit to Celsius\n" +
      "4. Convert from Fahrenheit to Kelvin\n" +
      "5. Convert from Kelvin to Celsius\n" +
      "6. Convert from Kelvin to Fahrenheit"
    )

def celsius_to_fahrenheit(temp):
    temp_fahrenheit = (9 / 5) * (temp) + 32
    return temp_fahrenheit

def celsius_to_kelvin(temp):
    temp_kelvin = (temp) + 273.15
    return temp_kelvin

def fahrenheit_to_celsius(temp):
    temp_celsius = (5 / 9) * (temp - 32)
    return temp_celsius

def fahrenheit_to_kelvin(temp):
    temp_kelvin = (5 / 9) * (temp - 32) + 273.15
    return temp_kelvin

def kelvin_to_celsius(temp):
    temp_celsius = temp - 273.15
    return temp_celsius

def kelvin_to_fahrenheit(temp):
    temp_fahrenheit = (9 / 5) * (temp - 273.15) + 32
    return temp_fahrenheit

#call to main function() ------------------------------
main()
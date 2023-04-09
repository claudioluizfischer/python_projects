# Name: Claudio Fischer
# UNumber - U92525778

'''
Description: 
This code defines a class called RetailItem which represents an item in a retail store with its name, 
number in inventory, and price. It has a constructor that initializes these attributes, and 
a __str__ method that returns a formatted string of the item's information.

The main() function prompts the user to input information for two RetailItem objects and then creates 
those objects using the provided input. It then prints a summary of the two items with their names, 
amount, and prices. Finally, it calls the main() function to execute the program.
'''

class RetailItem:
    def __init__(self, type, inventory_amount, price):
        self.__type = str(type)
        self.__inventory_amount = str(inventory_amount)
        self.__price = float(price)

    def __str__(self):
        return f"{self.__type.ljust(20)}{self.__inventory_amount.ljust(20)}${self.__price:.2f}"


def main():
    name1 = input("Name of item 1: ")
    amount1 = input("Amount of item 1: ")
    price1 = input("Price of item 1: ")

    name2 = input("\nName of item 2: ")
    amount2 = input("Amount of item 2: ")
    price2 = input("Price of item 2: ")

    #Creatingtwo RetailItem objects with the values specified by the user
    item1 = RetailItem(name1, amount1, price1)
    item2 = RetailItem(name2, amount2, price2)

    print("\nHere is a summary of the items you added:")
    print("Item".ljust(20), "Amount".ljust(20), "Price", sep="")
    print("---------------------------------------------------")
    print(item1)
    print(item2)

#--- call main() function ---
main()





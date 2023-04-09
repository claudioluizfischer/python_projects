'''
Claudio Fischer
U92525778
Description: This program inputs user's questions and outputs random responses from
20 different answers on the list. This uses a main function to verify if the user wants
to continue asking questions and generates numbers used to generate the random responses.
The main() function also calls the function response_generator() that prints the response
'''
import random as rn

def main():
    continue_validator = ''
    while(continue_validator.lower() != "no"):
        #r in range 1 to 20
        r = rn.randint(1, 20)
        input("What is your question? ")
        response_generator(r)
        continue_validator = input("Would you like to ask another question? ")

def response_generator(random_number):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    print(responses[random_number])

# ----- calling main function ----
main()
'''
Generates a random password based on a word or statement provided by the user.

Basically, the user will be asked what word or phrase they would like their 
password to be based on, and it generates a random password from that.

Each password must meet the following requirements:

1. At least one uppercase letter.
2. At least one lowercase letter.
3. At least one digit.
4. At least one special character.
5. 12 characters long.
'''
from random import choice, shuffle
import string as s, math


def replace_common_letters(statement):
    """
    Replace letters that have special characters that look similar to them.
    E.g replacing 'a' with '@'

    :param statement:
    """
    similarity_table = {
        "a": "@",
        "8": "&",
        "H": "#",
        "S": "$",
        "Z": "%",
        "z": "%",
        "X": "*",
        "O": "0"
    }

    # remove the whitespace
    statement = statement.strip()

    # replace each member of the table
    for key, value in similarity_table.items():
        statement = statement.replace(key,value)
    
    return statement


while True:
    # get the statement from the user
    user_statement = input("\n\nEnter a statement you want to make a password from: ")
    
    # if the statement is not up to four characters, notify user 
    if len(user_statement) < 4:
        print("\n\nStatement must be at least four characters long.\n\n")
        continue

    # remove extra whitespaces within the text, e.g. spaces and tabs
    user_statement = user_statement.replace(" ","").replace("\t","")

    # replace some letters with symbols
    user_statement = replace_common_letters(user_statement)
    
    # the user's statement will be padded with extra characters

    # generate two random lowercase letters
    lower_letters = "".join([choice(s.ascii_lowercase) for i in range(0,2)])

    # generate two random uppercase letters
    upper_letters = "".join([choice(s.ascii_uppercase) for i in range(0,2)])

    # generate two random digits
    digits = "".join([choice(s.digits) for i in range(0,2)])

    # generate two random special characters
    special_characters = "".join([choice(s.punctuation) for i in range(0,2)])

    # join then together and shuffle them to form the padding
    padding = lower_letters + upper_letters + digits + special_characters
    padding = list(padding)
    shuffle(padding)
    padding = "".join(padding)

    # Divide the padding into two parts, put the first part at the start 
    # and the second part at the end
    halfway = math.floor(len(padding)/2)
    start_padding = padding[:halfway]
    end_padding = padding[halfway:]

    # Add the start padding to the start of the statement,
    # and the end padding to the end of the statement to form the refined password
    password = f"{start_padding}{user_statement}{end_padding}"

    print(f"\n\nPassword: {password}\n")

    if input("\nContine Y/N? ").lower() == "n":
        break

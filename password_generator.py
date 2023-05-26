'''
Generates a random password.
Each password must meet the following requirements:

1. At least one uppercase letter.
2. At least one lowercase letter.
3. At least one digit.
4. At least one special character.
5. 12 characters long.
'''
from random import choice, shuffle
import string as s


while True:
    lower_letter = choice(s.ascii_lowercase)
    upper_letter = choice(s.ascii_uppercase)

    number = choice(s.digits)

    character = choice(s.punctuation)

    rest = "".join([choice(s.digits+s.ascii_letters+s.punctuation) for i in range(9)])

    password = f"{upper_letter}{lower_letter}{number}{character}{rest}"
    password = list(password)

    shuffle(password)

    password = "".join(password)

    print(f"Password: {password}")

    if input("Contine Y/N? ").lower() == "n":
        break

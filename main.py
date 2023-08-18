import random

characters = "abcdefghijklmnopqrstuvwxyz"

#password length
length = input("How many characters should the password be?\n")
length = int(length)

#case
case = input("Case sensitive? [Y/N]\n")
if case == "Y" or case == "y" or case == "yes" or case == "Yes" or case == "YES":
    case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters += case
elif case == "N" or case == "n" or case == "no" or case == "No" or case == "NO":
    case = ""
    characters = characters.replace(case, "")

#numbers
numbers = input("Numbers? [Y/N]\n")
if numbers == "Y" or numbers == "y" or numbers == "yes" or numbers == "Yes" or numbers == "YES":
    numbers = "1234567890"
    characters += numbers
elif numbers == "N" or numbers == "n" or numbers == "no" or numbers == "No" or numbers == "NO":
    numbers = ""
    characters = characters.replace(numbers, "")

#special
special = input("Type all special characters you want to allow, or press Enter for no special characters.\n")
characters += special

#password generation
password = ""
for c in range(length):
    password += random.choice(characters)

print(password)
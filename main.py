import random

characters = string.ascii_lowercase

#password length
length = int(input("How many characters should the password be?\n"))

#case
case = input("Case sensitive? [Y/N]\n").lower()
if case == "y" or case == "yes":
    case = string.ascii_uppercase
    characters += case
elif case == "n" or case == "no":
    characters = characters.replace(case, "")

#numbers
numbers = input("Numbers? [Y/N]\n").lower()
if numbers == "y" or numbers == "yes":
    numbers = "1234567890"
    characters += numbers
elif numbers == "n" or numbers == "no":
    characters = characters.replace(numbers, "")

#special
special = input("Type all special characters you want to allow, or press Enter for no special characters.\n")
characters += special

#password generation
password = ""
for c in range(length):
    password += random.choice(characters)

print(password)

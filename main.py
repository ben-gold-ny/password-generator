import random

# characters = "abcdefghijklmnopqrstuvwxyz"
characters = string.ascii_lowercase

#password length
length = int(input("How many characters should the password be?\n"))

#case
# case = input("Case sensitive? [Y/N]\n")
case = input("Case sensitive? [Y/N]\n").lower()
# if case == "Y" or case == "y" or case == "yes" or case == "Yes" or case == "YES":
if case == "y" or case == "yes":
    case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters += case
# elif case == "N" or case == "n" or case == "no" or case == "No" or case == "NO":
elif case == "n" or case == "no":
    # case = ""
    characters = characters.replace(case, "")

#numbers
# numbers = input("Numbers? [Y/N]\n")
numbers = input("Numbers? [Y/N]\n").lower()
# if numbers == "Y" or numbers == "y" or numbers == "yes" or numbers == "Yes" or numbers == "YES":
if numbers == "y" or numbers == "yes":
    numbers = "1234567890"
    characters += numbers
# elif numbers == "N" or numbers == "n" or numbers == "no" or numbers == "No" or numbers == "NO":
elif numbers == "n" or numbers == "no":
    # numbers = ""
    characters = characters.replace(numbers, "")

#special
special = input("Type all special characters you want to allow, or press Enter for no special characters.\n")
characters += special

#password generation
password = ""
for c in range(length):
    password += random.choice(characters)

print(password)

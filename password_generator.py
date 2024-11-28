import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

#Randomizing the letters based on the users input
selected_letters = ""
for final_letters in range(nr_letters):
    selected_letters += random.choice(letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))

#Randomizing the symbols based on the users input
selected_symbols = ""
for final_symbols in range(nr_symbols):
    selected_symbols += random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))

#Randomizing the numbers based on the users input
selected_numbers = ""
for final_numbers in range(nr_numbers):
    selected_numbers += random.choice(numbers)

#Putting all the characters together in one variable
password = selected_letters + selected_numbers + selected_symbols

#Randomizing the password variable to add complexity
randomized_password = list(password)
random.shuffle(randomized_password)

print(f"Your new password is: {"" .join(randomized_password)}")




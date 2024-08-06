import random
import data

print("Welcome to the Password Generator App!")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(number_of_letters):
    password_list.append(random.choice(data.letters))

for char in range(number_of_symbols):
    password_list.append(random.choice(data.symbols))

for char in range(number_of_numbers):
    password_list.append(random.choice(data.numbers))

randomized_password_list = random.sample(password_list, k=len(password_list))
password = ''

for item in randomized_password_list:
    password += item

print(password)

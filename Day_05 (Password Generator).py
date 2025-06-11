import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#easy version:

password_1 = []

for x in range(nr_letters):
    password_1 += random.choice(letters)
for x in range(nr_symbols):
    password_1 += random.choice(symbols)
for x in range(nr_numbers):
    password_1 += random.choice(numbers)

print(password_1)

#hard version:
password_1.clear()
password_2 = []
password_length = nr_letters + nr_numbers + nr_symbols

for x in range(nr_letters):
    password_1 += random.choice(letters)
for x in range(nr_symbols):
    password_1 += random.choice(symbols)
for x in range(nr_numbers):
    password_1 += random.choice(numbers)

characters_remaining = password_length

#The instructors solution bypasses this loop and just uses the
#random.shuffle() function, which does the same thing 
#it probably has a better time complexity though ¯\_(ツ)_/¯
for x in range(password_length):
    random_int = random.randint(0, characters_remaining-1)
    password_2 += password_1[random_int]
    password_1.pop(random_int)
    characters_remaining -= 1

print(password_2)
print(f"Your password is {password_2}")
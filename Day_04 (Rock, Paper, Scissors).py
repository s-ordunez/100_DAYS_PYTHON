import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_choice = int(input("""What do you choose? 
Type 0 for Rock, 1 for Paper or 2 for Scissors.
"""))
if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(choices[user_choice])
else:
    print("undefined")
print("""
Computer chose:
""")

computer_choice = random.randint(0,2)

print(choices[computer_choice])

if user_choice < computer_choice and computer_choice != 2:
    print("You win!")
elif user_choice > computer_choice and computer_choice == 2:
    print("You lose.")
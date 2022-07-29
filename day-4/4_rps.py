import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["R", "P", "S"]

choices = {
    "R": ("Rock",  rock),
    "P": ("Paper", paper),
    "S": ("Scissors", scissors)  
}

your_choice= input("Rock! Paper! Scissors! Type 'R' for rock, 'P' for paper and 'S' for scissors ").upper()
computer_choice = random.choice(options)
result = ""

if your_choice == options[0]:
    if computer_choice == options[0]:
        result  = "It's a draw."
    elif computer_choice == options[1]:
        result = "Computer Wins!"
    else:
        result = "You Win!"
elif your_choice == options[1]:
    if computer_choice == options[1]:
        result  = "It's a draw."
    elif computer_choice == options[2]:
        result = "Computer Wins!"
    else:
        result = "You Win!"
elif your_choice == options[2]:
    if computer_choice == options[2]:
        result  = "It's a draw."
    elif computer_choice == options[0]:
        result = "Computer Wins!"
    else:
        result = "You Win!"
else:
    result = "Invalid choice"


print(f"You chose: {choices[your_choice][0]}\n")
print(f"{choices[your_choice][1]}\n\n")

print(f"Computer chose: {choices[computer_choice][0]}\n")
print(f"{choices[computer_choice][1]}\n\n")

print(f"Result: {result}")

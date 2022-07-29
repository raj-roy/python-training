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

you_win_count =0
computer_win_count =0
draw_count = 0

while True:
    print("Press X to quit!")
    your_choice= input("Rock! Paper! Scissors! Type 'R' for rock, 'P' for paper and 'S' for scissors. ").upper()
    computer_choice = random.choice(options)
    result = ""

    if your_choice == "X":
        break

    if your_choice == options[0]:
        if computer_choice == options[0]:
            result  = "It's a draw."
            draw_count += 1
        elif computer_choice == options[1]:
            result = "Computer Wins!"
            computer_win_count += 1
        else:
            result = "You Win!"
            you_win_count += 1
    elif your_choice == options[1]:
        if computer_choice == options[1]:
            result  = "It's a draw."
            draw_count += 1
        elif computer_choice == options[2]:
            result = "Computer Wins!"
            computer_win_count += 1
        else:
            result = "You Win!"
            you_win_count += 1
    elif your_choice == options[2]:
        if computer_choice == options[2]:
            result  = "It's a draw."
            draw_count += 1
        elif computer_choice == options[0]:
            result = "Computer Wins!"
            computer_win_count += 1
        else:
            result = "You Win!"
            you_win_count += 1
    else:
        result = "Invalid choice. Computer Wins!"
        computer_win_count += 1



    print(f"You chose: {choices[your_choice][0]}\n")
    print(f"{choices[your_choice][1]}\n\n")

    print(f"Computer chose: {choices[computer_choice][0]}\n")
    print(f"{choices[computer_choice][1]}\n\n")

    print(f"Result: {result}")


print(f"You won {you_win_count} times.")
print(f"Computer won {computer_win_count} times.")
print(f"Draw {computer_win_count} times.")

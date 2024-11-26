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

game_images = [rock, paper, scissors]


player_choice = int(input("Welcome to Rock, Paper, Scissors!\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if player_choice == 0:
    print(game_images[0])
elif player_choice == 1:
    print(game_images[1])
elif player_choice == 2:
    print(game_images[2])
else:
    print("Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")

print("Computer chose:")
computer_choice = random.randint(0,2)
#print(computer_choice)

if computer_choice == 0:
    print(game_images[0])
elif computer_choice == 1:
    print(game_images[1])
else:
    print(game_images[2])

if player_choice > 2:
    print("You lose, please choose a valid number between 0 and 2.")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif player_choice < computer_choice:
    print("You lose")
elif player_choice == computer_choice:
    print("It's a draw uWu")
else: print("You win!")




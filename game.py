print("Welcome to Rock-Paper-Scissors!")
object = input("Choose rock, paper, or scissors: ")
object = object.lower()
print(f"You chose: {object}") 

import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("Computer chose:", computer_choice)
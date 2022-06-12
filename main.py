import random

options = ["R","P","S"]
choices = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}

def rules():
    print('''The Rules of the game are as follows
    Rock Smashes Scissors
    Paper Covers Rock
    Scissors Cuts Paper ''')

def human_choice():
    while True:
        human_choice = input('''Make your move: 
        R for Rock
        P for Paper
        S for Scissors: ''').upper()
        if human_choice in options:
            break
        else:
            print("Invalid Selection! Possible moves are R, P and S")
    return human_choice
def computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def is_not_tie(human, computer):
    print(f"Player ({choices[human]}) : CPU ({choices[computer]})")
    
    if (human == "R"):
        if (computer == "S"):
            print(f"You Win! {choices[human]} smashes {choices[computer]}")
        else:
           print(f"You Lose! {choices[computer]} covers {choices[human]}")
    elif (human == "P"):
        if (computer == "R"):
            print(f"You Win! {choices[human]} covers {choices[computer]}")
        else:
           print(f"You Lose! {choices[computer]} cuts {choices[human]}")
    elif (human == "S"):
        if (computer == "P"):
            print(f"You Win! {choices[human]} cuts {choices[computer]}")
        else:
           print(f"You Lose! {choices[computer]} smashes {choices[human]}")

def play_game():
    human = human_choice()
    computer = computer_choice()
    while human == computer:
        print(f"Player {human} : CPU {computer}")
        print("It's a tie!")
        human = human_choice()
        computer = computer_choice()
    is_not_tie(human, computer)

play_game()
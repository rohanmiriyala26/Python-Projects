import random
choices = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0
def get_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
        return "Computer"
    elif (player == "Rock" and computer == "Scissor") or (player == "Scissor" and computer == "Rock"):
        return "Player"
    elif (player == "Paper" and computer == "Scissor") or (player == "Scissor" and computer == "Paper"):
        return "Computer"
print("Welcome to Rock, Paper, Scissors Game!")
while True:
    player_choice = input("Choose Rock, Paper, or Scissor: ").capitalize()
    if player_choice not in choices:
        print("Invalid choice. Please pick Rock, Paper, or Scissor.")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    result = get_winner(player_choice, computer_choice)
    if result == "Tie":
        print("It's a tie!")
    elif result == "Computer":
        print(f"{computer_choice} beats {player_choice}. Computer wins this round.")
        computer_score += 1
    elif result == "Player":
        print(f"{player_choice} beats {computer_choice}. You win this round!")
        player_score += 1
    print(f"Score - You: {player_score}, Computer: {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

from game_logic import get_computer_choice, decide_winner
from until import get_user_choice, display_result

print("🎮 Welcome to Stone-Paper-Scissors Game!")

while True:  
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result = decide_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
def get_user_choice():
    user = input("Enter stone, paper, or scissors: ").lower()
    while user not in ["stone", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        user = input("Enter stone, paper, or scissors: ").lower()
    return user

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")
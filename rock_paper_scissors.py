import random

CHOICES = ['rock', 'paper', 'scissors']

BEATS = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif BEATS[user] == computer:
        return 'user'
    else:
        return 'computer'


def play_again():
    choice = input("Play again? (y/n): ").strip().lower()
    return choice in ('y', 'yes')


def rock_paper_scissors():
    print("=" * 40)
    print("       ROCK - PAPER - SCISSORS")
    print("=" * 40)
    print("Rock beats scissors, scissors beat paper, paper beats rock.\n")

    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

        if not play_again():
            break

        round_num += 1

    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you won overall!")
    elif user_score < computer_score:
        print("Computer won overall. Better luck next time!")
    else:
        print("Overall result: Tie!")

    print("Thanks for playing!")


if __name__ == "__main__":
    rock_paper_scissors()

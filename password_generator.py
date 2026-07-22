import random
import string


def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_yes_no(prompt):
    choice = input(prompt).strip().lower()
    return choice in ('y', 'yes')


def password_generator():
    print("Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Error: Length must be a positive number.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    print("\nChoose complexity options (y/n):")
    use_upper = get_yes_no("Include uppercase letters? ")
    use_digits = get_yes_no("Include numbers? ")
    use_symbols = get_yes_no("Include symbols? ")

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    password_generator()

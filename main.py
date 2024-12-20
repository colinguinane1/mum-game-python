import random

programmer = "Colin Guinane"

def play():
    min_num = 1
    max_num = 50
    num = random.randint(min_num, max_num)
    attempt = 0
    attempt_max = 5
    
    print(f"I'm thinking of a number between {min_num} and {max_num}, and I'll give you {attempt_max} tries to guess it.")

    while attempt < attempt_max:
        try:
            guess = int(input("Can you guess what it is: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < num:
            attempt += 1
            attempt_left = attempt_max - attempt
            print(f"Higher... {attempt_left} tries left.")
        elif guess > num:
            attempt += 1
            attempt_left = attempt_max - attempt
            print(f"Lower... {attempt_left} tries left.")
        else:  # guess == num
            print(f"That's correct! The number was {num}!")
            break

    if attempt == attempt_max:
        print(f"No guesses remaining... The number was {num}.")

    retry = input("Play again? (Y/N): ").strip().lower()
    if retry == "y":
        play()
    else:
        print("Thank you for playing!")
        print(f"Programmed by {programmer}")
        exit(0)

play()

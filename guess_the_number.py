from random import randrange

def get_level_max(level):
    return 10 + (level - 1) * 5

def get_guess(level):
    while True:
        guess = input(f"Level {level} Guess: ")
        if guess.isdigit() and int(guess) > 0:
            return int(guess)
        print("Enter a valid positive integer!")

def main():
    print("Welcome to Number Guessing Game!")
    level, total_score = 1, 0

    while True:
        print(f"\n--- Level {level} ---")
        target = randrange(1, get_level_max(level) + 1)
        attempts = 5

        while attempts:
            guess = get_guess(level)

            if guess == target:
                print(f"Correct! You've cleared Level {level}.")
                total_score += attempts * 10
                break

            print("Too high!" if guess > target else "Too low!")
            attempts -= 1
            print(f"Attempts left: {attempts}")
        else:
            print(f"Game Over! The number was {target}.")
            break

        print(f"Total Score: {total_score}")
        if input("Do you want to continue to the next level? (y/n): ").lower() != 'y':
            print(f"Thanks for playing! Final Score: {total_score}")
            break

        level += 1

if __name__ == "__main__":
    main()
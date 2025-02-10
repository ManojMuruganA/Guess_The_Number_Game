import random
import time

def get_random_number(level):
    if level == 1:
        return random.randint(10, 99)  # Ensuring a 2-digit number
    elif level == 2:
        return random.randint(100, 999)  # Ensuring a 3-digit number

def provide_clues(number, level):
    print("Clues:")
    if level == 1:
        print(f"1. The number is {'even' if number % 2 == 0 else 'odd'}.")
        print("2. The number is a 2-digit number.")
    elif level == 2:
        print(f"1. The number is {'even' if number % 2 == 0 else 'odd'}.")
        print("2. The number is a 3-digit number.")
        print(f"3. The sum of the digits is {sum_of_digits(number)}.")

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def get_user_guess(attempt):
    while True:
        try:
            return int(input(f"Attempt {attempt}: Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    print("Welcome to the Guess the Number game!")
    print("Rules:")
    print("1. You will be provided with clues to guess a number.")
    print("2. Level 1: Guess a 2-digit number. Level 2: Guess a 3-digit number.")
    print("3. You have 6 chances to guess the number.")
    
    total_score = 0 
    
    while True:
        level = int(input("Enter the level (1 for 2-digit, 2 for 3-digit): "))
        if level not in [1, 2]:
            print("Invalid level. Please enter 1 or 2.")
            continue
        
        number_to_guess = get_random_number(level)
        provide_clues(number_to_guess, level)
        
        for attempt in range(1, 7):
            user_guess = get_user_guess(attempt)
            if number_to_guess == user_guess:
                print("Congratulations! You guessed the correct number.")
                total_score += 7 - attempt 
                break
            elif number_to_guess < user_guess:
                print("The guessed number is greater than the actual number.")
            else:
                print("The guessed number is smaller than the actual number.")
        else:
            print(f"Sorry, you've run out of chances. The correct number was {number_to_guess}.")
        
        print(f"Your score for this round: {total_score}")
        
        if total_score >= 5:
            print("\nCelebration Time! 🎇🎆🎇")
            for i in range(8, 0, -1):
                print(" \\" * i)
                time.sleep(0.2)
        
        play_again = input("Do you want to play again? (Enter 'y' for yes, any other key to exit): ").lower()
        if play_again != 'y':
            break
    
    print("Thanks for playing!")

play_game()

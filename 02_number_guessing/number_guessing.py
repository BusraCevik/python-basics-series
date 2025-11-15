# This is a simple number guessing game.
# The program asks the user to enter an upper limit for the random number.
# It then generates a random number between 0 and the given limit.
# The user tries to guess the number, and the program gives hints ("Go higher" or "Go lower") until the correct number is guessed.
# It also validates that the user inputs numbers and counts the number of guesses made.

import random

top_of_range = input("Please enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a number larger than 0")

else:
    print("Please type a number")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number ")
        continue

    if user_guess == random_number:
        print("You guessed right!")
        break
    elif user_guess > random_number:
        print("Go lower ")
    else:
        print("Go higher ")
print("You got it in", guesses, "guesses")


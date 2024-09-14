import random

print("""Welcome to number guesser!!
Select the difficulty and then on each chance, enter a number""")

# Prompt for difficulty
difficulty = int(input("""What difficulty? :
1 = Easy (0 - 10)
2 = Medium (0 - 25)
3 = Hard (0 - 50)
"""))

# Set the range of numbers based on the difficulty level
if difficulty == 1:
    print("You selected Easy")
    number = random.randint(0, 10)
elif difficulty == 2:
    print("You selected Medium")
    number = random.randint(0, 25)
elif difficulty == 3:
    print("You selected Hard")
    number = random.randint(0, 50)
else:
    print("Invalid difficulty selected! Exiting the game.")
    exit()

# While loop to keep asking for guesses until the correct number is guessed
guessed = False  # This flag will track whether the user has guessed correctly

while not guessed:
    guess = int(input("Guess a number: "))

    # Check if the guessed number is correct
    if guess == number:
        print("Congratulations! You guessed the right number!")
        guessed = True  # Set guessed to True to exit the loop
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

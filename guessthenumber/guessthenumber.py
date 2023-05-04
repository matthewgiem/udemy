# import modules
import random
import art

#global variables
random_number = random.randint(1,100)
turns = 0

# home screen
print(art.guess_the_number)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Psst, the correct answer is {random_number}")
easy_or_hard = input("Choose a dificulty. Type 'easy' or 'hard':").lower()

# game logic
if easy_or_hard == "easy":
    turns = 10
elif easy_or_hard == "hard":
    turns = 5
else:
    print("you didn't select a valid difficulity")

while turns > 0:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < random_number:
        print("Too low.")
        turns -= 1
        if turns == 0:
            print("You've run out of guesses, you lose")
            break
        print("Guess agian")
    if guess > random_number:
        print("Too high.")
        turns -= 1
        if turns == 0:
            print("You've run out of guesses, you lose")
            break
        print("Guess agian")
    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        break





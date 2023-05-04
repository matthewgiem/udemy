# import modules
import random
import art

print(art.guess_the_number)

random_number = random.randint(1,100)

def home_screen(number):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst, the correct answer is {number}")
    input("Choose a dificulty. Type 'easy' or 'hard':")

home_screen(random_number)

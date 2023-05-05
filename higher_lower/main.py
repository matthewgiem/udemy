import random
import game_data
import art
import os

score = 0
game_list = game_data.data
random.shuffle(game_list)

def compare_followers(A, B):
    if A['follower_count'] > B['follower_count']:
        return True
    else:
        return False

def select_opponunt(old):
    return old, game_list.pop()

first = game_list.pop()
second = game_list.pop()

while True:
    os.system("clear")
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {first['name']} a {first['description']}, from {first['country']}")
    print(art.vs)
    print(f"Against B: {second['name']} a {second['description']}, from {second['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        if compare_followers(first, second):
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    if choice == 'b':
        if not compare_followers(first, second):
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    first, second = select_opponunt(second)
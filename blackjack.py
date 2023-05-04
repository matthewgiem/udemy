import random
import os
import time
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cards_dict = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10, "A": 1}

def remove_cards_from_deck(list_of_cards, deck):
    for x in list_of_cards:
        deck.remove(x)
    return deck

def deal_x_cards(deck, x):
    hand = random.sample(deck, k=x)
    deck = remove_cards_from_deck(list_of_cards=hand, deck=deck)
    return hand, deck

def check_total(players_hand):    
    how_many_Aces = 0
    for x in players_hand:
        if x == "A":
            how_many_Aces += 1
    total = 0
    for x in players_hand:
        total += cards_dict[x]
    aces_total = total
    if how_many_Aces != 0:
        aces_total += 10
    if aces_total > 21:
        return total, aces_total
    if how_many_Aces != 0:
        return aces_total, total
    return total, aces_total

def check_for_over_21(hand):
    if hand[0] > 21:
        return True
    else:
        return False

def in_game(end=True):
    return end

def print_screen(players, dealers):
    os.system("clear")
    print(f"Your Cards: {players}")
    print(f"Your Score is {check_total(players)[0]}")
    print(f"Dealers First Card: {dealers[0]}")
    print(f"Dealers Score is {check_total(dealers[0])[0]}")

def print_screen_dealer(players, dealers):
    os.system("clear")
    print(f"Your Cards: {players}")
    print(f"Your Score is {check_total(players)[0]}")
    print(f"Dealers Cards: {dealers}")
    print(f"Dealers Score is {check_total(dealers)[0]}")
    print(f"The Dealer has {check_total(dealers_hand)[0]} points and will {dealer_logic(dealers_hand)}")

def dealer_logic(dealer):
    if check_total(dealer)[0] <= 17:
        print(check_total(dealer)[0])
        return "hit"
    else:
        return "stay"

def who_won(players, dealers):
    if check_for_over_21(check_total(players)):
        print("You Lose!")
    elif check_for_over_21(check_total(dealers)):
        print("You Win")
    elif check_total(players)[0] > check_total(dealers)[0]:
        print("You Win")
    elif check_total(players)[0] == check_total(dealers)[0]:
        print("Its a Tie You Lose")
    else:
        print("You Lose")


players_hand, cards = deal_x_cards(cards,2)
dealers_hand, cards = deal_x_cards(cards,2)


os.system("clear")
while in_game():
    while not check_for_over_21(check_total(players_hand)):
        print_screen(players_hand, dealers_hand)
        hit = input("Type 'y' to get another card, tpye 'n' to pass: ").lower()
        if hit == 'y':
            card_to_add, cards = deal_x_cards(cards,1)
            players_hand.append(card_to_add[0])
        if hit == 'n':
            break
        if check_total(players_hand)[0] == 21:
            break

    if check_total(players_hand)[0] == 21:
        print_screen(players_hand, dealers_hand)
        print("21")
        print("You Win")
        input("Press Enter to continue...")
        break
    if not check_for_over_21(check_total(players_hand)):
        input("Press Enter to continue")
        if dealer_logic(dealers_hand) == "hit":
            print_screen_dealer(players_hand, dealers_hand)
            
            input("Press Enter to continue...")
            card_to_add, cards = deal_x_cards(cards, 1)
            dealers_hand.append(card_to_add[0])
            print_screen_dealer(players_hand, dealers_hand)
            input("Press Enter to continue...")
        if dealer_logic(dealers_hand) == "stay":
            print(f"The Dealer has {check_total(dealers_hand)[0]} points and will {dealer_logic(dealers_hand)}")
            print_screen_dealer(players_hand, dealers_hand)
            who_won(players_hand, dealers_hand)
            input("Press Enter to continue...")
            break
    if  check_for_over_21(check_total(players_hand)):
        print_screen(players_hand, dealers_hand)
        print("You're busted")
        print("Game Over")
        input("Press Enter to continue...")
        break

    



        
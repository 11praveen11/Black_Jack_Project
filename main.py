import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Tie😶!"
    elif c_score == 0:
        return "You Lost😔, The Dealer got Blackjack!!"
    elif u_score == 0:
        return "You Won🏅, It's a Blackjack!"
    elif u_score > 21:
        return "You went over😔, You Loose!"
    elif c_score > 21:
        return "You Won🏅, Dealer went over!"
    elif u_score > c_score:
        return "You Won🏅, You have the highest number!"
    else:
        return "You Lost😔, Dealer has the highest number!"

def play_game():
    print(art.logo)
    print("Please note, If you or the Dealer hit Blackjack in the first attempt. your score is considered as '0' ")
    user_cards = []
    dealer_cards = []
    dealer_score = -1
    user_score = -1
    game_over = False


    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nyour cards: {user_cards}.  user score: {user_score}")
        print(f"Dealer first card: {dealer_cards[0]}\n")


        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'H' to HIT or 'S' to STAND ")
            if another_card.lower() == 'h':
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"your final cards: {user_cards}.  Total score: {user_score}")
    print(f"Dealer's final cards: {dealer_cards}.  Total score: {dealer_score}")
    print(compare(user_score, dealer_score))


play_again = True
while play_again:
    play_again = input("\nDo you want to play a game of Blackjack? 'Y' for yes, 'N' for no: ").lower()
    if play_again == 'n':
        play_again = False
        print("Thank you, visit again!")
    elif play_again == 'y':
        print("\n" * 20)
        play_game()




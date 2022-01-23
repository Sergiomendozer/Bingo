import random
# B = 1 - 15
# I = 16 - 30
# N = 31 - 45
# G = 46 - 60
# O = 61 - 75

def random_bingo_number():
    bingo_numbers = ["B-15","B-11", "B-12"]
    chosen_bingo_number = random.choice(bingo_numbers)
    print (chosen_bingo_number)
    return (chosen_bingo_number)

random_bingo_number()
#the list is a regular full deck of cards
    # full_deck_of_cards = [A+S, "2"+S, "3"+S, "4"+S, "5"+S, "6"+S, "7"+S, "8"+S, "9"+S, "10"+S, K+" "+S, Q+" "+S, J+S,A+C, "2"+C, "3"+C, "4"+C, "5"+C, "6"+C, "7"+C, "8"+C, "9"+C, "10"+C, K+" "+C, Q+" "+C, J+C,A+D, "2"+D, "3"+D, "4"+D, "5"+D, "6"+D, "7"+D, "8"+D, "9"+D, "10"+D, K+" "+D, Q+" "+D, J+D,A+H, "2"+H, "3"+H, "4"+H, "5"+H, "6"+H, "7"+H, "8"+H, "9"+H, "10"+H, K+" "+H, Q+" "+H, J+H]
    # #shuffles if needs it
    # playing_deck = (shuffle_reshuffle(full_deck_of_cards,playing_deck))
    # chosen_card = random.choice(playing_deck)
    # #to draw and take out card that is used, to avoid having the same cards being played
    # take_out_of_deck = playing_deck.index(chosen_card)
    # playing_deck.pop(take_out_of_deck)
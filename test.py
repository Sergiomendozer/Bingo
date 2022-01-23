import random
END = '\033[0m'

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White
def random_bingo_number():
    bingo_numbers = [Green + "B-15" +END, Blue + "B-11" + END, Red + "B-12" + END]
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
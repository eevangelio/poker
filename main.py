from library.Poker import Poker

deckID = ""


def poker_game():
    print("Welcome to Poker Game!!!\n")
    print("Press 'S' and Enter keys to shuffle card...")
    while True:
        userinput = input()
        if userinput == "S" or userinput == "s":
            b = Poker.shuffle_cards()
            deckID = b
            break
        else:
            print("Invalid input")

    drawnumber = 0
    print("Press 'D' to draw cards\nPress 'X' to exit")
    while True:
        userinput = input()
        if userinput == "D" or userinput == "d":
            draw_and_lay(deckID)
            drawnumber = drawnumber + 1
        elif userinput == "X" or userinput == "x":
            print("Thank you! Goodbye!")
            exit()
        else:
            print("Invalid input!")

        if drawnumber == 10:
            print("Maximum number of draw cards for a deck has been reached...exiting...")
            break
        else:
            print("Press 'D' to draw cards\nPress 'X' to exit")


def draw_and_lay(deckID):
    c = Poker.draw_cards(deckID)
    code = Poker.json_extract(c, "code")
    value = Poker.json_extract(c, "value")
    suit = Poker.json_extract(c, "suit")

    Poker.show_card_on_hand(value, suit)
    remapped = Poker.sort_cards(code)

    result = Poker.get_winning_combination(remapped)
    print("Highest-scoring hand is: {result}\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    poker_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

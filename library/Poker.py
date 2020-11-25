import requests


class Poker:
    def __init__(self, test):
        self.test = test

    @staticmethod
    def shuffle_cards():
        """
        This method creates and shuffles a new deck of cards
        Uses the requests library to call HTTP GET REST API
        """
        response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        temp = response.json()
        return temp["deck_id"]

    def shuffle_remaining_cards(deckID):
        """
        This method shuffles the remaining cards in the deck
        Uses the requests library to call HTTP GET REST API
        """
        response = requests.get(f"https://deckofcardsapi.com/api/deck/{deckID}/shuffle/")
        temp = response.json()

    def draw_cards(deckID):
        """
        This method draws 5 cards from the deck
        Uses the requests library to call HTTP GET REST API
        """
        response = requests.get(f"https://deckofcardsapi.com/api/deck/{deckID}/draw/?count=5")
        temp = response.json()
        return temp

    def show_card_on_hand(value, suit):
        """
        This method is used to show the initial card on hand
        """
        print("Card On hand:")
        for x in range(5):
            print(" - " + str(value[x]) + " " + str(suit[x]))

    def sort_cards(hand):
        """
        This method sorts the card based on the numerical value
        This method also makes some substitutions to the values
        - A -> 1
        - J -> 11
        - Q -> 12
        - K -> 13
        also adds leading 0 for numbers 2-9
        makes 0 -> 10
        """
        remapped = []
        for x in range(5):
            test = hand[x]
            value = test[0]
            suit = test[1]
            if test[0] == "A":
                value = '01'
            elif test[0] == "J":
                value = 11
            elif test[0] == "Q":
                value = 12
            elif test[0] == "K":
                value = 13
            elif test[0] == "0":
                value = 10
            else:
                value = '0' + str(value)
            newcode = str(value) + suit
            remapped.append(newcode)
        remapped.sort()
        return remapped

    def get_winning_combination(hand):
        """This method is used to determine the highest pointing card combination"""

        def is_five_of_a_kind(handValues):
            """This sub-method is used to determine if the card on hand is a five of a kind"""
            isWinner = False
            if (handValues[0] == handValues[1]) and (handValues[1] == handValues[2]) and (handValues[2] == handValues[3]) and (handValues[3] == handValues[4]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_straight_flush(handValues, handSuit):
            """This sub-method is used to determine if the card on hand is a straight flush"""
            isWinner = False
            if (is_straight(handValues)):
                if (is_flush(handSuit)):
                    isWinner = True
                else:
                    isWinner = False
            else:
                isWinner = False
            return isWinner

        def is_four_of_kind(handValues):
            """This sub-method is used to determine if the card on hand is a four of a kind"""
            isWinner = False
            if (handValues[0] == handValues[1]) and (handValues[1] == handValues[2]) and (handValues[2] == handValues[3]) and (handValues[3] != handValues[4]):
                isWinner = True
            elif (handValues[0] != handValues[1]) and (handValues[1] == handValues[2]) and (handValues[2] == handValues[3]) and (handValues[3] == handValues[4]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_full_house(handValues):
            """This sub-method is used to determine if the card on hand is a full house"""
            isWinner = False
            if (handValues[0] == handValues[1]) and (handValues[1] == handValues[2]) and (handValues[3] == handValues[4]) and (handValues[2] != handValues[3]):
                isWinner = True
            elif (handValues[2] == handValues[3]) and (handValues[3] == handValues[4]) and (handValues[0] == handValues[1]) and (handValues[1] != handValues[2]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_flush(handSuit):
            """This sub-method is used to determine if the card on hand is a flush"""
            isWinner = False
            if (handSuit[0] == handSuit[1]) and (handSuit[1] == handSuit[2]) and (handSuit[2] == handSuit[3]) and (handSuit[3] == handSuit[4]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_straight(handValues):
            """This sub-method is used to determine if the card on hand is a straight"""
            isWinner = False
            if (handValues[0] == 1) and (handValues[1] == 10) and ((handValues[1] + 1) == handValues[2]) and ((handValues[2] + 1) == handValues[3]) and ((handValues[3] + 1) == handValues[4]):
                isWinner = True
            elif ((handValues[0] + 1) == handValues[1]) and ((handValues[1] + 1) == handValues[2]) and ((handValues[2] + 1) == handValues[3]) and ((handValues[3] + 1) == handValues[4]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_three_of_a_kind(handValues):
            """This sub-method is used to determine if the card on hand is a three of a kind"""
            isWinner = False
            if (handValues[0] == handValues[1]) and (handValues[1] == handValues[2]) and (handValues[2] != handValues[3]) and (handValues[2] != handValues[4]) and (handValues[3] != handValues[4]):
                isWinner = True
            elif (handValues[1] == handValues[2]) and (handValues[2] == handValues[3]) and (handValues[0] != handValues[1]) and (handValues[3] != handValues[4]) and (handValues[0] != handValues[4]):
                isWinner = True
            elif (handValues[2] == handValues[3]) and (handValues[3] == handValues[4]) and (handValues[0] != handValues[1]) and (handValues[1] != handValues[2]) and (handValues[0] != handValues[2]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_two_pair(handValues):
            """This sub-method is used to determine if the card on hand is a three of a two pair"""
            isWinner = False
            if handValues[0] == handValues[1] and handValues[2] == handValues[3] and handValues[3] != handValues[4] and handValues[1] != handValues[2]:
                isWinner = True
            elif handValues[1] == handValues[2] and handValues[3] == handValues[4] and handValues[0] != handValues[1] and handValues[2] != handValues[3]:
                isWinner = True
            elif handValues[0] == handValues[1] and handValues[3] == handValues[4] and handValues[1] != handValues[2] and handValues[2] != handValues[3]:
                isWinner = True
            else:
                isWinner = False
            return isWinner

        def is_one_pair(handValues):
            """This sub-method is used to determine if the card on hand is a one pair"""
            isWinner = False
            if (handValues[0] == handValues[1]) and (handValues[1] != handValues[2]) and (handValues[2] != handValues[3]) and (handValues[3] != handValues[4]):
                isWinner = True
            elif (handValues[0] != handValues[1]) and (handValues[1] == handValues[2]) and (handValues[2] != handValues[3]) and (handValues[3] != handValues[4]):
                isWinner = True
            elif (handValues[0] != handValues[1]) and (handValues[1] != handValues[2]) and (handValues[2] == handValues[3]) and (handValues[3] != handValues[4]):
                isWinner = True
            elif (handValues[0] != handValues[1]) and (handValues[1] != handValues[2]) and (handValues[2] != handValues[3]) and (handValues[3] == handValues[4]):
                isWinner = True
            else:
                isWinner = False
            return isWinner

        """There is no sub-method for determining whether high card, it is the default if all tests above fail"""

        values = []
        suits = []

        """converting the list of string values to list of integer values"""
        for x in range(5):
            test = hand[x]
            if test[0] == "0":
                values.append(int(test[1]))
            else:
                values.append(int(test[0:2]))
            suits.append(test[2])

        """
        call the sub-method tests
        once a test is found immediately return the rank back to method caller as string
        default is high card
        """
        if is_five_of_a_kind(values):
            return "Five of a kind!"
        elif is_straight_flush(values, suits):
            return "Straight Flush!"
        elif is_four_of_kind(values):
            return "Four of a kind!"
        elif is_full_house(values):
            return "Full House!"
        elif is_flush(suits):
            return "Flush!"
        elif is_straight(values):
            return "Straight!"
        elif is_three_of_a_kind(values):
            return "Three of a kind!"
        elif is_two_pair(values):
            return "Two pair!"
        elif is_one_pair(values):
            return "One pair!"
        else:
            return "High card!"

    def json_extract(obj, key):
        """Recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values

# Card Deck Exercise

#### Requirements:
1. Using a dec of cards API (https://deckofcardsapi.com/), implement a Python app that does the following:
    - Creates and shuffles a deck of cards 
    - Draws 5 cards from the hand and prints their numbers and suits to the console 
    - Identifies the top scoring poker hand (https://en.wikipedia.org/wiki/List_of_poker_hands) that the cards fulfill and prints it to the console
2. Include some tests that validate the portion of your code that identifies the highest-scoring hand (the tests should not contain any API requests, and instead use mock data).
3. Please create a public GitHub repository with the code, and include a README file with:
    - Instructions for running the program and tests
    - Any assumptions you made while coding
    
#### Getting Started
To get a local copy up and running follow these simple steps.

#### Prerequisites
- python 3
- requests library

#### Installation
1. Clone the repo

        git clone https:///github.com/eevangelio/poker.git

#### Usage
- To run the main app
    - navigate to the poker directory
    - execute 

            python main.py
        
    - at the prompt type in "S" and press enter to Create a shuffled deck of cards
    - type "D" to draw five cards
    - type "X" to exit
- To run the unit test
    - navigate to the poker directory
    - execute 
    
            python test_card_combination.py

### Assumptions
- I used the standard 52 card deck
- There will be a total of 10 card draws per shuffle. The program will exit after the 10th draw.


### Code
##### library/Poker.py
- shuffle_cards
    - used to create or instantiate a deck of cards
    - uses the requests library to call the HTTP GET "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1" REST API
    - returns the "deck_id" back to the caller
- draw_cards
    - expects a parameter "deck_id"
    - uses the requests library to call the HTTP GET "https://deckofcardsapi.com/api/deck/{deckID}/draw/?count=5" REST API
    - returns a json object response back to the caller
- show_card_on_hand
    - expects two parameters; list of values and list of suits
    - prints to the console the values and suits combination of cards in hand
- sort_cards
    - expects a parameter of cards list using "code"
    - sorts the cards based on their numerical values
        - replaces A with 1, J with 11, Q with 12, and K with 13
        - adds leading zeros for numbers 2-9
        - adds number 1 to 0 to make it 10
    - returns a sorted list of cards based on values
- get_winning_combination
    - expects a sorted list of cards
    - subjects the list against different winning card scenarios
    - returns a string of the determined high-scoring card combination
 
##### test_card_combination.py
- implements unittest
    - test_straight_flush_card
    - test_four_of_a_kind
    - test_full_house
    - test_flush
    - test_straight
    - test_three_of_a_kind
    - test_two_pair
    - test_one_pair
    - test_high_card
 - all of the above test cases use mock data
        
    
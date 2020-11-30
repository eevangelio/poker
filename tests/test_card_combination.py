from library.Poker import Poker

import unittest


class MyTestCase(unittest.TestCase):
    def test_straight_flush_card(self):
        result = Poker.get_winning_combination(['01S', '02S', '03S', '04S', '05S'])
        self.assertEqual(result, "Straight Flush!")
        result = Poker.get_winning_combination(['06C', '07C', '08C', '09C', '10C'])
        self.assertEqual(result, "Straight Flush!")
        result = Poker.get_winning_combination(['09H', '10H', '11H', '12H', '13H'])
        self.assertEqual(result, "Straight Flush!")
        result = Poker.get_winning_combination(['07D', '08D', '09D', '10D', '11D'])
        self.assertEqual(result, "Straight Flush!")
        result = Poker.get_winning_combination(['01H', '10H', '11H', '12H', '13H'])
        self.assertEqual(result, "Straight Flush!")

    def test_four_of_a_kind(self):
        result = Poker.get_winning_combination(['01S', '01C', '01H', '01D', '05S'])
        self.assertEqual(result, "Four of a kind!")
        result = Poker.get_winning_combination(['01S', '05C', '05H', '05D', '05S'])
        self.assertEqual(result, "Four of a kind!")

    def test_full_house(self):
        result = Poker.get_winning_combination(['01S', '01C', '01H', '03D', '03S'])
        self.assertEqual(result, "Full House!")
        result = Poker.get_winning_combination(['01S', '01C', '03H', '03D', '03S'])
        self.assertEqual(result, "Full House!")

    def test_flush(self):
        result = Poker.get_winning_combination(['01S', '03S', '05S', '07S', '09S'])
        self.assertEqual(result, "Flush!")
        result = Poker.get_winning_combination(['01C', '03C', '05C', '07C', '09C'])
        self.assertEqual(result, "Flush!")
        result = Poker.get_winning_combination(['01H', '03H', '05H', '07H', '09H'])
        self.assertEqual(result, "Flush!")
        result = Poker.get_winning_combination(['01D', '03D', '05D', '07D', '09D'])
        self.assertEqual(result, "Flush!")

    def test_straight(self):
        result = Poker.get_winning_combination(['01D', '02H', '03C', '04S', '05S'])
        self.assertEqual(result, "Straight!")
        result = Poker.get_winning_combination(['09D', '10H', '11C', '12S', '13S'])
        self.assertEqual(result, "Straight!")
        result = Poker.get_winning_combination(['04D', '05H', '06C', '07S', '08S'])
        self.assertEqual(result, "Straight!")
        result = Poker.get_winning_combination(['01D', '10H', '11C', '12S', '13S'])
        self.assertEqual(result, "Straight!")

    def test_three_of_a_kind(self):
        result = Poker.get_winning_combination(['01D', '01H', '01C', '04S', '05S'])
        self.assertEqual(result, "Three of a kind!")
        result = Poker.get_winning_combination(['01D', '02H', '02C', '02S', '03S'])
        self.assertEqual(result, "Three of a kind!")
        result = Poker.get_winning_combination(['01D', '02H', '03C', '03S', '03H'])
        self.assertEqual(result, "Three of a kind!")

    def test_two_pair(self):
        result = Poker.get_winning_combination(['01D', '01H', '02C', '02S', '03S'])
        self.assertEqual(result, "Two pair!")
        result = Poker.get_winning_combination(['01D', '02H', '02C', '03S', '03H'])
        self.assertEqual(result, "Two pair!")
        result = Poker.get_winning_combination(['01D', '01H', '02C', '03S', '03H'])
        self.assertEqual(result, "Two pair!")

    def test_one_pair(self):
        result = Poker.get_winning_combination(['01D', '01H', '02C', '03S', '04H'])
        self.assertEqual(result, "One pair!")
        result = Poker.get_winning_combination(['01D', '02H', '02C', '03S', '04H'])
        self.assertEqual(result, "One pair!")
        result = Poker.get_winning_combination(['01D', '02H', '03C', '03S', '04H'])
        self.assertEqual(result, "One pair!")
        result = Poker.get_winning_combination(['01D', '02H', '03C', '04S', '04H'])
        self.assertEqual(result, "One pair!")

    def test_high_card(self):
        result = Poker.get_winning_combination(['01D', '03H', '05C', '07S', '09H'])
        self.assertEqual(result, "High card!")
        result = Poker.get_winning_combination(['02D', '04H', '06C', '08S', '10H'])
        self.assertEqual(result, "High card!")

if __name__ == '__main__':
    unittest.main(verbosity=2)

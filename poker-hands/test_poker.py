import unittest
import poker


class TestPokerHands(unittest.TestCase):
    # Tests that parse_hand() correctly separates the cards, ranks, and suits 
    def test_parse_hand(self):
        hand = poker.parse_hand("10S,10H,4D,7C,2S")

        self.assertEqual(
            hand,
            {
                "cards": ["10S", "10H", "4D", "7C", "2S"],
                "ranks": ["10", "10", "4", "7", "2"],
                "suits": ["S", "H", "D", "C", "S"]
            }
        )

    def test_pair(self):
        hand = poker.parse_hand("10S,10H,4D,7C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "pair")

    def test_two_pair(self):
        hand = poker.parse_hand("9S,9H,4D,4C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "two_pair")

    # Test that three matching ranks are classified as three of a kind
    def test_three_of_a_kind(self):
        hand = poker.parse_hand("10S,10H,10D,7C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "three_of_a_kind")

    # Test that a hand with no matching ranks is classified as high card
    def test_high_card(self):
        hand = poker.parse_hand("2S,5H,7D,9C,KS")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "high_card")

    # Test that a hand with three cards of one rank and two cards of another rank is a full house
    def test_full_house(self):
        hand = poker.parse_hand("10S,10H,10D,KC,KS")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "full_house")

    # Test that five cards with the same suit are classified as a flush
    def test_flush_is_not_a_straight(self):
        hand = poker.parse_hand("2S,5S,9S,JS,KS")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "flush")

    # Test that four cards have the same rank
    def test_four_of_a_kind(self):
        hand = poker.parse_hand("10S,10H,10D,10C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "four_of_a_kind")

    def test_flush_is_not_a_straight(self):
        hand = poker.parse_hand("2S,5S,9S,JS,KS")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "flush")

    def test_ace_low_straight(self):
        hand = poker.parse_hand("AS,2H,3D,4C,5S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "straight")

    def test_full_house(self):
        hand = poker.parse_hand("10S,10H,10D,KC,KS")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "full_house")

    def test_straight_flush_beats_four_of_a_kind(self):
        straight_flush = poker.parse_hand("5S,6S,7S,8S,9S")
        four_of_a_kind = poker.parse_hand("QS,QH,QD,QC,2S")
        self.assertEqual(poker.compare_hands(straight_flush, four_of_a_kind), "a")

    def test_tiebreak_by_kicker(self):
        pair_of_kings = poker.parse_hand("KS,KH,4D,7C,2S")
        pair_of_tens = poker.parse_hand("10S,10H,QD,JC,9S")
        self.assertEqual(poker.compare_hands(pair_of_kings, pair_of_tens), "a")


if __name__ == "__main__":
    unittest.main()

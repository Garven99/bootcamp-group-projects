import unittest
import poker


class TestPokerHands(unittest.TestCase):
    def test_pair(self):
        hand = poker.parse_hand("10S,10H,4D,7C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "pair")

    def test_two_pair(self):
        hand = poker.parse_hand("9S,9H,4D,4C,2S")
        category, _ = poker.classify_hand(hand)
        self.assertEqual(category, "two_pair")

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

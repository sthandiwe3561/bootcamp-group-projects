RANK_ORDER = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14,
}

SUITS = {"S", "H", "D", "C"}

HAND_RANKS = [
    "high_card",
    "pair",
    "two_pair",
    "three_of_a_kind",
    "straight",
    "flush",
    "full_house",
    "four_of_a_kind",
    "straight_flush",
]


def parse_hand(text):
    cards = [card.strip() for card in text.split(",")]
    ranks = [card[:-1] for card in cards]
    suits = [card[-1] for card in cards]

    return ...


def classify_hand(hand):
    raise NotImplementedError("This function is not implemented yet.")


def compare_hands(hand_a, hand_b):
    raise NotImplementedError("This function is not implemented yet.")

good= "morning"

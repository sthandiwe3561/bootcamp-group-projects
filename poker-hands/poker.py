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

# return is returning the above values in a dictionary form
    return {
        "cards": cards,
        "ranks": ranks,
        "suits": suits
    }


def classify_hand(hand):
     #Split the work in statement
    #1st statement that going to check if this is a straight flush
    #2nd statement that going to check if this is a straight flush
    #3rd statement that going to check if this is a four of a kind
    #4th statement that going to check if this is a full house
    #5th  statement that going to check if this is a flush
    #6th statement that going to check if this is a straight
    #7th statement that going to check if this is a three of a kind
    #8th statement that going to check if this is a two pair
    #Otherwise it a pair

    #rerurn a dictionary tha will have hand rank and catagory for both hands
    raise NotImplementedError("This function is not implemented yet.")


def compare_hands(hand_a, hand_b):
    raise NotImplementedError("This function is not implemented yet.")


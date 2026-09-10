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

        # Loop through the ranks in the hand, find their integer values,
    # and store them in rank_values

    # created empty list to store ranks integer values
    rank_values = []

    for rank in hand["ranks"]:
        value = RANK_ORDER[rank]
        rank_values.append(value)

    # These conditions define the rules for each hand category.
    # We check the strongest categories first so that a hand is given
    # the highest category it qualifies for.

    # Create an empty list to store how many times each rank appears.
    counts = []

    # STRAIGHT FLUSH
    # Consecutive ranks AND all five cards have the same suit.
    # Add condition later.

    # FOUR OF A KIND
    # One rank appears four times and another rank appears once.
    if 4 in counts and 1 in counts:
        return "four_of_a_kind"

    # FULL HOUSE
    # One rank appears three times and another rank appears twice.
    elif 3 in counts and 2 in counts:
        return "full_house"

    # FLUSH
    # All five cards have the same suit.
    # Add condition later.

    # STRAIGHT
    # Five ranks are consecutive.
    # Puts numbers in order from lowest to highest
    sorted_rank = sorted(rank_values)


    # THREE OF A KIND
    # One rank appears three times and the other two ranks appear once.
    elif 3 in counts and counts.count(1) == 2:
        return "three_of_a_kind"

    # TWO PAIR
    # Two different ranks appear twice and one rank appears once.
    elif counts.count(2) == 2 and 1 in counts:
        return "two_pair"

    # PAIR
    # One rank appears twice and the other three ranks appear once.
    elif 2 in counts and counts.count(1) == 3:
        return "pair"

    # HIGH CARD
    # All five ranks are different and do not form a straight.
    # Add the straight check before this condition.
    elif counts == [1, 1, 1, 1, 1]:
        return "high_card"
        
    
        #rerurn a dictionary tha will have hand rank and catagory for both hands
    raise NotImplementedError("This function is not implemented yet.")
    





def compare_hands(hand_a, hand_b):
    raise NotImplementedError("This function is not implemented yet.")


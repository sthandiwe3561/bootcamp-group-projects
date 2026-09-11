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

    # creeate empty list to store the integer values of the ranks
    rank_values = []

    for rank in hand["ranks"]:
        value = RANK_ORDER[rank]
        

    # These conditions define the rules for each hand category.
    # We check the strongest categories first so that a hand is given

    # Create an empty list to store how many times each rank appears.
    counts = []
    comparing_list = []

    for i in rank_values:
        if i not in comparing_list:
            count = rank_values.count(i)
            counts.append(count)
            comparing_list.append(i)

    
        

    # STRAIGHT FLUSH
    # Consecutive ranks AND all five cards have the same suit.
    # Add condition later.
    if len(set(hand["suits"])) == 1:
        sorted_ranks = sorted(rank_values)

        #Check for Ace-low straight:
        if sorted_ranks == [2, 3, 4, 5, 14]:
            return "straight_flush", comparing_list

        # Check for regular straight
        if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] + 5)):
            return "straight_flush", comparing_list
        
        # Same suite but not consecutive ranks, so it's a flush
        return "flush", comparing_list

    # FOUR OF A KIND
    # One rank appears four times and another rank appears once.
    # function checks the count of each rank. Rank appears four times
    elif 4 in counts:
        return "four_of_a_kind", comparing_list

    # FULL HOUSE
    # One rank appears three times and another rank appears twice.
    elif 3 in counts and 2 in counts:
        return "full_house", comparing_list

    # STRAIGHT
    # Five ranks are consecutive.
    #Checks if 1 appears 5 times in counts 
    elif counts.count(1)==5:
        # Arranges the numbers from highest to lowest 
        sorted_rank = sorted(rank_values)
        #lower straight(A-14 so LS needs seperate condition)
        if sorted_rank==[2,3,4,5,14]:
            return "straight" , comparing_list
         #is_straight is a variable that assume the hand is already straight
         # stores the restults of the loop
        is_straight = True
          
         #loop checks if the above variable is true,by check if the pervious number plus 1 equals the previous number
         # if one of the numbers plus one dont equal the number after it, it returns False and breaks the loop
         #if they dont equal it will returns True and it returns straight
        for i in range(4):
            if sorted_rank[i+1] != sorted_rank[i]+1:
                is_straight = False
                break
            
        if is_straight:
            return "straight", comparing_list
        
        return "high_card",  comparing_list



    # THREE OF A KIND
    # One rank appears three times and the other two ranks appear once.
    elif counts.count(3) == 1:
        return "three_of_a_kind", comparing_list

    # TWO PAIR
    # Two different ranks appear twice and one rank appears once.
    elif counts.count(2) == 2:
    
            pair_rank = None
    
            for i in rank_values:
                if rank_values.count(i) == 2:
                    pair_rank = i
    
            remaining_ranks = []
    
            for i in rank_values:
                if i != pair_rank:
                    remaining_ranks.append(i)
    
            remaining_ranks.sort(reverse=True)
    
            comparing_list = [pair_rank] + remaining_ranks
    
            return "two_pair", comparing_list
    

    # PAIR
    # One rank appears twice and the other three ranks appear once.
    elif counts.count(2) == 1:

        pair_rank = None

        for i in rank_values:
            if rank_values.count(i) == 2:
                pair_rank = i

        remaining_ranks = []

        for i in rank_values:
            if i != pair_rank:
                remaining_ranks.append(i)

        remaining_ranks.sort(reverse=True)

        comparing_list = [pair_rank] + remaining_ranks

        return "pair", comparing_list

        

    





def compare_hands(hand_a, hand_b):
    raise NotImplementedError("This function is not implemented yet.")


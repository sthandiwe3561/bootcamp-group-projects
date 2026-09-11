#psuedo code
BEGIN

    INPUT 5 playing cards

    EXTRACT the rank and suit of each card

    SORT the card ranks from lowest to highest

    COUNT how many times each rank appears

    IF all 5 cards have the same suit AND
       the ranks are consecutive
        OUTPUT "Straight Flush"

    ELSE IF there are 4 cards with the same rank
        OUTPUT "Four of a Kind"

    ELSE IF there are 3 cards with the same rank AND
            2 cards with another same rank
        OUTPUT "Full House"

    ELSE IF all 5 cards have the same suit
        OUTPUT "Flush"

    ELSE IF the ranks are consecutive
        OUTPUT "Straight"

    ELSE IF there are 3 cards with the same rank
        OUTPUT "Three of a Kind"

    ELSE IF there are 2 pairs of cards with the same rank
        OUTPUT "Two Pair"

    ELSE IF there are 2 cards with the same rank
        OUTPUT "One Pair"

    ELSE
        OUTPUT "High Card"

END

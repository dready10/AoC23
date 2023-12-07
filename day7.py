### Chat Log: https://chat.openai.com/share/fe6eddff-dcde-42a9-81f9-23f9204fbdd7

### This was a weird one. Part 1 didn't really work out of the gate, though it was close.
### I didn't help by basically not believing chatGPT on how one python function worked.
### After so long of incorrect solutions (even after providing the correct answer for
### the example, which I was intentionally trying to avoid doing), I eventually tested
### python's sort to see that, actually, it did work as chatGPT described.
### After that, it took like 5 seconds to fix the problem in part 1.

### Part 2 was the Land Of Edge Cases. Because chatGPT seemed to have a tenuous grasp
### on testing edge cases (or even correctly determining whether its output was correct)
### I had it write the skeleton of the algorithm and then very heavily adjusted it
### to make it work. I can't say if this was faster or slower than just starting from
### scratch.

### But oh boy do I have to say that not reading the problem closely enough caused
### problems. ChatGPT missed that in ties Jacks become 1s, and because I didn't read
### closely and mostly read the outputted code, I missed it too. As a result, writing
### the algorithm on my own was fraught with errors. Ultimately I found some additional
### test cases and their results so I could debug my algorithm. This is a cautionary
### tale about ChatGPT: you have to understand what you're asking it. If you don't, you
### can't fix the issues.

from collections import Counter

### The important function for part 1
def classify_hand_detailed(hand):
    """
    Classifies the hand into one of the Camel Cards types and returns a tuple
    that can be used to sort the hands. This includes the type of the hand and
    the card strengths in the original order.
    """
    card_strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 
                     '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    counts = Counter(hand)

    # Determine hand type
    if len(counts) == 1:
        # Five of a kind
        return (7, [card_strength[c] for c in hand])
    elif len(counts) == 2:
        if 4 in counts.values():
            # Four of a kind
            return (6, [card_strength[c] for c in hand])
        else:
            # Full house
            return (5, [card_strength[c] for c in hand])
    elif len(counts) == 3:
        if 3 in counts.values():
            # Three of a kind
            return (4, [card_strength[c] for c in hand])
        else:
            # Two pair
            return (3, [card_strength[c] for c in hand])
    elif len(counts) == 4:
        # One pair
        return (2, [card_strength[c] for c in hand])
    else:
        # High card
        return (1, [card_strength[c] for c in hand])

### The important function for Part 2
def find_best_hand_with_jokers(hand):
    """
    Determines the strongest hand type that can be formed with the given hand
    considering jokers (J). Jokers can act as any card to form the best possible hand.
    Jokers have a card strength of 1 for the purpose of breaking ties.
    """
    counts = Counter(hand)
    num_jokers = counts['J']
    del counts['J']  # Remove jokers for simplification

    # Early return for non-joker hands and five jokers hand
    if num_jokers == 0:
        return classify_hand_detailed(hand)
    if hand == "JJJJJ":
        return (7, [1, 1, 1, 1, 1])

    classified_hand = classify_hand_detailed(hand)

    # Function to replace J strength with 1 for tie-breaking
    def replace_joker_strength(card_strengths):
        return [1 if strength == 11 else strength for strength in card_strengths]

    # Check if a stronger hand can be formed with jokers
    for hand_type, required_count in [(7, 5), (6, 4)]:
        if any(count + num_jokers >= required_count for count in counts.values()):
            return (hand_type, replace_joker_strength(classified_hand[1]))

    # Check for full house
    if num_jokers == 1 and len(counts) == 2:
        return (5, replace_joker_strength(classified_hand[1]))

    # Check for three of a kind
    if any(count + num_jokers == 3 for count in counts.values()):
        return (4, replace_joker_strength(classified_hand[1]))

    # Default case: One pair with a joker
    return (2, replace_joker_strength(classified_hand[1]))

### Does the easy stuff for parts 1 and 2
def total_winnings_detailed(hands):
    """
    Calculates the total winnings for a list of hands with their bids, correctly handling ties.
    """
    classified_hands = [(classify_hand_detailed(hand.split()[0]), int(hand.split()[1])) for hand in hands]
    jokered_hands = [(find_best_hand_with_jokers(hand.split()[0]), int(hand.split()[1])) for hand in hands]

    # Sort the hands based on their classification, correctly handling ties
    classified_hands.sort(key=lambda x: x[0])
    jokered_hands.sort(key=lambda x: x[0])
    with open('inputs/day7o.txt', 'w') as f:
        for hand in jokered_hands:
            f.write(f'{hand}\n')
    # Calculate total winnings
    total = 0
    for rank, (_, bid) in enumerate(classified_hands, 1):
        total += bid * rank

    total_j = 0

    for rank, (_, bid) in enumerate(jokered_hands, 1):
        total_j += bid * rank

    return (total, total_j)

with open('inputs/day7.txt', 'r') as f:
    hands = f.readlines()

# Calculate total winnings
print(total_winnings_detailed(hands))
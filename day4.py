# Chat log: https://chat.openai.com/share/80cd6443-93ac-45c7-b309-dcba21ff23e3

def calculate_points(cards):
    total_points = 0

    for card in cards:
        winning_numbers, player_numbers = card.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        player_numbers = map(int, player_numbers.split())

        matches = 0
        for num in player_numbers:
            if num in winning_numbers:
                matches += 1

        if matches > 0:
            card_points = 2 ** (matches - 1)  # 1 point for the first, double for each additional
            total_points += card_points

    return total_points

# Test the function with the provided example
example_cards = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

print(calculate_points(example_cards))

with open('inputs/day4.txt') as f:
    cards = [c[1][0:-1] for c in [l.split(': ') for l in f.readlines()]]
print(cards)
print(calculate_points(cards))

def calculate_total_scratchcards(cards):
    # Convert each card into winning and player numbers
    card_details = [card.split(" | ") for card in cards]
    card_details = [(set(map(int, winning.split())), set(map(int, player.split())))
                    for winning, player in card_details]

    # Function to count matches
    def count_matches(winning_numbers, player_numbers):
        return len(winning_numbers.intersection(player_numbers))

    # Initialize total cards count with the original cards
    total_cards = len(cards)
    copies_won = [0] * len(cards)  # Track copies won for each card

    # Process each card to count matches and determine copies won
    for i, (winning_numbers, player_numbers) in enumerate(card_details):
        matches = count_matches(winning_numbers, player_numbers)
        # Distribute copies to subsequent cards
        for j in range(1, matches + 1):
            if i + j < len(cards):
                copies_won[i + j] += 1

    # Process the copies
    for i, copies in enumerate(copies_won):
        winning_numbers, player_numbers = card_details[i]
        matches = count_matches(winning_numbers, player_numbers)
        for _ in range(copies):
            total_cards += 1  # Count the copy
            # Distribute copies from this copy
            for j in range(1, matches + 1):
                if i + j < len(cards):
                    copies_won[i + j] += 1

    return total_cards

# Re-run the function with the provided example
print(calculate_total_scratchcards(cards))
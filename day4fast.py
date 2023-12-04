def part1(cards):
    card_details = [card.split(" | ") for card in cards]
    card_details = [(set(map(int, winning.split())), set(map(int, player.split())))
                    for winning, player in card_details]
    
    points = 0
    for card in card_details:
        points += (2 ** (len(card[0].intersection(card[1]))-1)) // 1
    return int(points)

def part2(cards):
    # Convert each card into winning and player numbers
    card_details = [card.split(" | ") for card in cards]
    card_details = [(set(map(int, winning.split())), set(map(int, player.split())))
                    for winning, player in card_details]
    
    num_winners_per_card = {}
    for i, card in enumerate(card_details):
        num_winners_per_card[i] = len(card[0].intersection(card[1]))
    
    card_counts = {}
    for i in range(len(num_winners_per_card.keys())):
        card_counts[i] = 1
    for i in num_winners_per_card:
        for j in range(1, num_winners_per_card[i]+1):
            card_counts[i+j] += 1 * card_counts[i]
    return sum(card_counts.values())

example_cards = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

with open('inputs/day4.txt') as f:
    cards = [c[1][0:-1] for c in [l.split(': ') for l in f.readlines()]]
print(part1(cards))
print(part2(cards))
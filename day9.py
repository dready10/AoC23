### Chat Log: https://chat.openai.com/share/587288a0-8407-4100-a411-aa4f3b8066d8

### Nothing much to say on this one. Just copying and pasting solutions. I didn't
### even need to correct or help, I didn't even read the problem before justing
### pasting it into ChatGPT. Incredible.

def extrapolate_next_value(history):
    """
    Function to extrapolate the next value of a given history.

    :param history: List of integers representing the history.
    :return: The extrapolated next value.
    """
    # Generate sequences of differences until all values are zero
    sequences = [history]
    while not all(v == 0 for v in sequences[-1]):
        sequences.append([y - x for x, y in zip(sequences[-1], sequences[-1][1:])])

    # Work out the next value in each sequence from the bottom up
    for i in range(len(sequences) - 1, 0, -1):
        next_diff = sequences[i][-1]
        next_value = sequences[i-1][-1] + next_diff
        sequences[i-1].append(next_value)

    # The next value of the original history is the last value of the first sequence
    return sequences[0][-1]

def extrapolate_previous_value(history):
    """
    Function to extrapolate the previous value of a given history.

    :param history: List of integers representing the history.
    :return: The extrapolated previous value.
    """
    # Generate sequences of differences until all values are zero
    sequences = [history]
    while not all(v == 0 for v in sequences[-1]):
        sequences.append([y - x for x, y in zip(sequences[-1], sequences[-1][1:])])

    # Work out the previous value in each sequence from the bottom up
    for i in range(len(sequences) - 1, 0, -1):
        prev_diff = sequences[i][0]
        prev_value = sequences[i-1][0] - prev_diff
        sequences[i-1].insert(0, prev_value)

    # The previous value of the original history is the first value of the first sequence
    return sequences[0][0]

with open('inputs/day9.txt') as f:
    histories = [[int(x) for x in line.split()] for line in f.readlines()]

    # Calculate the sum of extrapolated values for the provided examples
    sum_of_extrapolated_values = sum(extrapolate_next_value(history) for history in histories)
    print(sum_of_extrapolated_values)
    
    sum_of_extrapolated_previous_values = sum(extrapolate_previous_value(history) for history in histories)
    print(sum_of_extrapolated_previous_values)

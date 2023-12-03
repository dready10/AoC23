# Chat log: https://chat.openai.com/share/2086e799-895a-45a8-a80e-a99cbe585fa9

def sum_adjacent_numbers(grid):
    def is_non_period_symbol(ch):
        return not ch.isalnum() and ch != '.'

    def is_valid_position(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def extract_number(i, j):
        number = ''
        while j < len(grid[0]) and grid[i][j].isdigit():
            number += grid[i][j]
            j += 1
        return int(number), j

    def has_adjacent_symbol(x, y, num_length):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            for k in range(num_length):
                nx, ny = x + dx, y + dy + k
                if is_valid_position(nx, ny) and is_non_period_symbol(grid[nx][ny]):
                    return True
        return False

    total_sum = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            if grid[i][j].isdigit():
                number, new_j = extract_number(i, j)
                if has_adjacent_symbol(i, j, new_j - j):
                    total_sum += number
                j = new_j
            else:
                j += 1
        i += 1

    return total_sum

# Example usage
with open('inputs/day3.txt', 'r') as f:
    map_grid = [line[0:-1] for line in f.readlines()]
#map_grid = [
#    "12.3",
#    "*7.8",
#    ".9.."
#]


print(sum_adjacent_numbers(map_grid))

def extract_complete_number(grid, i, j):
    if not grid[i][j].isdigit():
        return None

    # Initialize the number with the digit at (i, j)
    number = grid[i][j]

    # Scan left from (i, j)
    left = j - 1
    while left >= 0 and grid[i][left].isdigit():
        number = grid[i][left] + number
        left -= 1

    # Scan right from (i, j+1)
    right = j + 1
    while right < len(grid[0]) and grid[i][right].isdigit():
        number += grid[i][right]
        right += 1

    return int(number)

def sum_multiplications_around_asterisks(grid):
    def is_valid_position(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    total_sum = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 directions

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                numbers = set()
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if is_valid_position(nx, ny) and grid[nx][ny].isdigit():
                        number = extract_complete_number(grid, nx, ny)
                        if number is not None:
                            numbers.add(number)

                # Multiplying all unique pairs of numbers found around the asterisk
                numbers = list(numbers)
                for k in range(len(numbers)):
                    for l in range(k + 1, len(numbers)):
                        total_sum += numbers[k] * numbers[l]

    return total_sum

print(sum_multiplications_around_asterisks(map_grid))
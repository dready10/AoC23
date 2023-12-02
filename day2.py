# Chat Log: https://chat.openai.com/share/71e68e1f-3b1c-4b56-9055-fd66ac306713

# Part 1
def sum_valid_game_ids(file_path):
    sum_ids = 0
    import os
    print(os.getcwd())
    with open(file_path, 'r') as file:
        for line in file:
            game_id, game_data = line.split(':')
            game_id = int(game_id.strip().split(' ')[1])  # Extracting the game number

            is_valid_game = True
            matches = game_data.split(';')
            for match in matches:
                colors = match.split(',')
                red, green, blue = 0, 0, 0

                for color in colors:
                    num, col = color.strip().split(' ')
                    num = int(num)
                    if col == 'red':
                        red = num
                    elif col == 'green':
                        green = num
                    elif col == 'blue':
                        blue = num

                    if red > 12 or green > 13 or blue > 14:
                        is_valid_game = False
                        break

                if not is_valid_game:
                    break

            if is_valid_game:
                sum_ids += game_id

    print(f"Sum of valid game IDs: {sum_ids}")

# Part 2
def sum_of_max_products(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            _, game_data = line.split(':')
            max_red, max_green, max_blue = 0, 0, 0

            matches = game_data.split(';')
            for match in matches:
                colors = match.strip().split(',')
                red, green, blue = 0, 0, 0

                for color in colors:
                    num, col = color.strip().split(' ')
                    num = int(num)
                    if col == 'red':
                        red = num
                    elif col == 'green':
                        green = num
                    elif col == 'blue':
                        blue = num

                max_red = max(max_red, red)
                max_green = max(max_green, green)
                max_blue = max(max_blue, blue)

            total_sum += max_red * max_green * max_blue

    print(f"Sum of the products of maximums: {total_sum}")

# Call the function with the path to your file
sum_valid_game_ids('inputs/day2.txt')

# Call the function with the path to your file
sum_of_max_products('inputs/day2.txt')


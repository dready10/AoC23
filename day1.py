# Chat Log: https://chat.openai.com/share/889634ff-1300-4232-9e8d-42a6e218ec2c

## Part One
def sum_of_concatenated_digits(file_path):
    """
    Reads a file line by line, extracts the first and last numerical digits from each line,
    concatenates them, and sums these values across all lines.
    """
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            digits = [char for char in line if char.isdigit()]
            if digits:
                first_digit = digits[0]
                last_digit = digits[-1]
                concatenated_value = int(first_digit + last_digit)
                total_sum += concatenated_value
    return total_sum

# Part 2
def sum_concatenated_values(input_file_path):
    """
    Processes each line of the input file character by character.
    When a number word is found, replaces the first character of the word with the digit.
    Then, takes the first digit and the last digit in the line, concatenates them,
    and sums these concatenated values across all lines.
    """
    number_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    def process_line(line):
        processed_line = ""
        i = 0
        while i < len(line):
            replaced = False
            for word, digit in number_words.items():
                if line[i:].startswith(word):
                    processed_line += digit  # Replace only the first character of the number word
                    replaced = True
                    break
            if not replaced:
                processed_line += line[i]
            i += 1
        return processed_line

    total_sum = 0
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            processed_line = process_line(line.strip())

            # Extract first and last digit
            digits = [char for char in processed_line if char.isdigit()]
            if len(digits) >= 2:
                concatenated_value = int(digits[0] + digits[-1])
                total_sum += concatenated_value
            elif len(digits) == 1:
                concatenated_value = int(digits[0] * 2)
                total_sum += concatenated_value

    return total_sum


# The file path is now set to "inputs/day1.txt"
file_path = 'inputs/day1.txt'

# Run the function and print the output
output = sum_of_concatenated_digits(file_path)
print(output)

output = sum_concatenated_values(file_path)
print(output)
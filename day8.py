from math import gcd

### Chat log: https://chat.openai.com/share/344290d3-9198-49a2-8769-9b391d6c3c4f

### Boy chatGPT made this a breeze. Part 1 was literally copy and paste the problem in,
### copy and paste the solution out. Part 2 was also super easy. It was basically,
### paste in the additional information, get a solution that was too slow, and then
### point it to the mathematically faster answer. Honestly, doing part 2 myself would
### have taken like 20 times as long to figure out how to derive the periodicity and
### the lcms between them. Instead, it took like 2 minutes to describe the problem
### and test this.

### Except for the with block at the bottom to read in input, this code is 100%
### from chatGPT with no adjustments from me.

### Part 1
def navigate_desert(instructions, nodes):
    # Parsing the nodes into a dictionary
    node_dict = {}
    for node in nodes:
        key, value = node.split(' = ')
        node_dict[key] = tuple(value.strip('()').split(', '))

    # Navigating through the nodes
    current_node = 'AAA'
    steps = 0
    instruction_index = 0

    while current_node != 'ZZZ':
        # Determine the direction (Left or Right)
        direction = instructions[instruction_index]

        # Update the current node
        current_node = node_dict[current_node][0 if direction == 'L' else 1]

        # Move to the next instruction, looping back if necessary
        instruction_index = (instruction_index + 1) % len(instructions)

        # Increment step count
        steps += 1

    return steps

### Part 2
def lcm(a, b):
    """Compute the least common multiple of a and b."""
    return abs(a*b) // gcd(a, b)

def find_route_periodicity_and_initial(nodes, instructions, start_node):
    """
    Find the periodicity and the initial step count at which the route from 
    the start_node first completes. Returns a tuple (periodicity, initial_step).
    """
    current_node = start_node
    steps = 0
    instruction_index = 0

    # Run the instructions once to find the initial completion step
    while not current_node.endswith('Z'):
        direction = instructions[instruction_index]
        current_node = nodes[current_node][0 if direction == 'L' else 1]
        instruction_index = (instruction_index + 1) % len(instructions)
        steps += 1

    initial_step = steps

    # Run the instructions again to find the periodicity
    while True:
        direction = instructions[instruction_index]
        current_node = nodes[current_node][0 if direction == 'L' else 1]
        instruction_index = (instruction_index + 1) % len(instructions)
        steps += 1

        if current_node.endswith('Z'):
            break

    periodicity = steps - initial_step

    return periodicity, initial_step

def find_lowest_common_step(nodes, instructions):
    # Parsing the nodes into a dictionary
    node_dict = {}
    for node in nodes:
        key, value = node.split(' = ')
        node_dict[key] = tuple(value.strip('()').split(', '))

    # Identifying starting nodes (nodes ending with 'A')
    start_nodes = [node for node in node_dict.keys() if node.endswith('A')]

    # Find the periodicity and initial step for each route
    routes = [find_route_periodicity_and_initial(node_dict, instructions, node) for node in start_nodes]

    # Calculate the least common multiple of the periodicities
    periodicities = [route[0] for route in routes]
    overall_periodicity = 1
    for p in periodicities:
        overall_periodicity = lcm(overall_periodicity, p)

    # Adjust for initial offsets to find the lowest common step count
    common_step = overall_periodicity
    for periodicity, initial_step in routes:
        while common_step % periodicity != initial_step % periodicity:
            common_step += overall_periodicity

    return common_step


with open('inputs/day8.txt', 'r') as f:
    lines = f.readlines()
    instructions = lines[0][:-1]
    nodes = [line[:-1] for line in lines[2:]]
    print(navigate_desert(instructions, nodes))
    print(find_lowest_common_step(nodes, instructions))
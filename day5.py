### Chat log: https://chat.openai.com/share/51278931-1c08-47e8-b598-e2501bd8a4ba

### Comments that begin with ### are written by me. Comments with one # are
### from chatGPT. The ### contain some of my thoughts.

def parse_mapping_section(lines):
    """ Parse a mapping section from the input file into a list of tuples """
    mappings = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            mappings.append(tuple(map(int, parts)))
    return mappings

def read_and_process_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Parse seeds
    seeds_line = lines[0]
    seeds = list(map(int, seeds_line[len('seeds: '):].split()))

    # Splitting the file into sections for each mapping
    sections = ''.join(lines[2:]).split('map:')
    mappings = [parse_mapping_section(section.strip().split('\n')) for section in sections if section.strip()]

    return seeds, mappings

def map_number(number, mapping):
    """ Map a number from one category to its corresponding number in the next category. """
    for dest_start, src_start, length in mapping:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number

def process_seeds(seeds, mappings):
    """ Process each seed through the sequence of mappings to find the corresponding location numbers. """
    location_numbers = []
    for seed in seeds:
        current_number = seed
        for mapping in mappings:
            current_number = map_number(current_number, mapping)
        location_numbers.append(current_number)
    return location_numbers

# Read and process the input file
seeds, mappings = read_and_process_input('input.txt')

### Part 1
# Now we can process the seeds with the existing functions
location_numbers = process_seeds(seeds, mappings)
min_location_number = min(location_numbers)
print(min_location_number)

### Part 2
### This is the version chatGPT produced with only minor adjustments to get the
### logic right. For instance, the switch to while initial ranges: instead of
### what was an originally a for loop so that I could process and remap remaining
### parts of seed ranges that were only partially mapped.
### It basically works, but it's off by one somewhere.
def split_and_remap_ranges(initial_ranges, mapping):
    """ Split and remap the initial ranges based on the given mapping. """
    if len(mapping) == 0:
        return initial_ranges

    new_ranges = []
    while initial_ranges:
        range_to_check = initial_ranges.pop(0)
        start, end = range_to_check
        overlapped = False
        for dst_start, src_start, length in mapping:
            src_end = src_start + length
            dst_end = dst_start + length

            if src_start > end or src_end < start:
                # No overlap with the current range
                continue

            overlapped = True

            # Calculate overlapping part
            overlap_start = max(start, src_start)
            overlap_end = min(end, src_end)

            # Map the overlapping part
            mapped_start = dst_start + (overlap_start - src_start)
            mapped_end = min(mapped_start + (overlap_end - overlap_start), dst_end)

            # Add the mapped range to new ranges
            new_ranges.append((mapped_start, mapped_end))

            # Adjust the original range to exclude the overlapping part
            if not (start >= src_start and end <= src_end):
                if start < overlap_start:
                    initial_ranges.append((start, overlap_start - 1))
                if end > overlap_end:
                    start = overlap_end + 1
                    initial_ranges.append((start, end))

        if not overlapped:
            new_ranges.append((start, end))

    return new_ranges

### So I rewrote the above algorithm, but blind, basically not referencing
### chatGPT's version. It's mainly different in how it calculates the 
### new start and end ranges, as well the language (but not the math) 
### behind re-apending the partially unmapped ranges, but mathematically I
### think they should be the same. In fact, when I replace those parts
### of chatGPT's with my parts, I still get the same off-by-one error
### in chatGPT's version.
### So.... I dunno lol. But this one works! 
def my_remap(current_ranges, mapping):
    new_ranges = []
    ranges_to_check:list = current_ranges
    while ranges_to_check:
        checking_range = ranges_to_check.pop(0)
        start, end = checking_range
        overlapped = False
        for dst, src, ln in mapping:
            src_end = src+ln

            if end < src or start > src_end:
                continue
            
            overlapped = True
 
            overlap_startsat = max(src, start)
            overlap_endsat = min(src_end, end)
            overlap_length = overlap_endsat - overlap_startsat

            new_start = dst + (overlap_startsat - src)
            new_end = new_start + overlap_length
            new_ranges.append((new_start, new_end))

            if start < src:
                ranges_to_check.append((start, src-1))
            if end > src_end:
                ranges_to_check.append((src_end+1, end))

        if not overlapped:
            new_ranges.append((start, end))

    return new_ranges

# the remap function needs to take something with a (start, end) range, but seeds are
# given as (start, length); remapping that. (ChatGPT did not realize this, it's a
# realization I came to when debugging.)
current_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
for mapping in mappings:
    current_ranges = my_remap(current_ranges, mapping)

# If current_ranges is not empty, find the lowest number in the final set of ranges
if current_ranges:
    lowest_location_number = min([start for start, end in current_ranges])
else:
    lowest_location_number = "No valid location numbers found."
print(lowest_location_number)

# Open the input file

sections_file = open("sections.txt", "r")

# Initialise a list of lines from the file

sections_pairs = sections_file.readlines()

# Initialise empty list for storing ranges

sections_ranges = []

# Create function to check if ranges overlap for Part 2


def overlaps(pair_range1, pair_range2):
    for i in pair_range1:
        if i in pair_range2:
            return True

    for j in pair_range2:
        if j in pair_range1:
            return True

    return False


# Iterate over lines of the file

for line in sections_pairs:

    # Initialise a variable to store each boundary of the ranges

    section = ""

    # Initialise lists for the boundaries of each range

    pair1 = []
    pair2 = []

    # Remove the new line escape character from each line

    line.replace("\n", "")

    # Iterate over the characters of each line

    for char in line:

        # Add each boundary to the range and then to the list of ranges

        try:
            int(char)
            section += char

        except ValueError:

            if len(pair1) < 2:
                pair1.append(int(section))
                section = ""

            else:
                pair2.append(int(section))
                section = ""

    sections_ranges.append([pair1, pair2])

count = 0

# Part 1

# Iterate over each range

for pair in sections_ranges:
    range1 = range(pair[0][0], pair[0][1])
    range2 = range(pair[1][0], pair[1][1])

    # Finding ranges contained in another

    if (range1.start >= range2.start and range1.stop <= range2.stop) or \
            (range2.start >= range1.start and range2.stop <= range1.stop):
        count += 1

print(count)

# Pair 2

count = 0

# Iterate over each range again

for pair in sections_ranges:
    range1 = range(pair[0][0], pair[0][1] + 1)
    range2 = range(pair[1][0], pair[1][1] + 1)

    # Finding each range that overlaps the other from that pair

    if overlaps(range1, range2):
        count += 1

print(count)

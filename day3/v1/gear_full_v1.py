# schematic = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..',
#     ]

schematic = []
parts = []
valid_parts = []
symbols = []
gears = []

def find_symbols(line):
    for char in line:
        if not char.isdigit() and char != '.' and char not in symbols:
            symbols.append(char)

def check_adjacent(schematic, idx, char_idx):
    isAdjacentVal = False
    adjacent_indices = [
            (idx-1, char_idx),  # above
            (idx+1, char_idx),  # below
            (idx, char_idx-1),  # left
            (idx, char_idx+1),  # right
            (idx-1, char_idx-1),  # above-left
            (idx+1, char_idx-1),  # below-left
            (idx-1, char_idx+1),  # above-right
            (idx+1, char_idx+1),  # below-right
        ]
    for i, j in adjacent_indices:
            # Check if the indices are within bounds
            if 0 <= i < len(schematic) and 0 <= j < len(schematic[0]):
                adjacent_char = schematic[i][j]
                # print(adjacent_char)
                if adjacent_char in symbols:
                    isAdjacentVal = True
                    # print(f"Adjacent to {schematic[idx][char_idx]} at ({idx}, {char_idx}): {adjacent_char}")
    return isAdjacentVal

with open('gear_input.txt', 'r') as file:
    schematic = file.readlines()
    for line in schematic:
        find_symbols(line.strip())
    for idx,line in enumerate(schematic):
        part = ''
        part_start_idx = None
        isValid = False
        for char_idx,char in enumerate(line.strip()):
            if char == '*':
                gears.append((idx,char_idx))
            if char.isdigit() and char != '.':
                if part_start_idx == None:
                    part_start_idx = char_idx
                part += char
                if not isValid:
                    # check all 8 adjacent locations
                    isValid = check_adjacent(schematic, idx, char_idx)
            elif part: 
                if isValid:
                    valid_parts.append([int(part), idx, (part_start_idx, char_idx)])
                else:
                    parts.append([int(part), idx, (part_start_idx, char_idx)])
                part = ''
                isValid = False
                part_start_idx = None
            if len(line.strip()) == char_idx+1:
                if part:
                    if isValid:
                        valid_parts.append([int(part), idx, (part_start_idx, char_idx)])
                    else:
                        parts.append([int(part), idx, (part_start_idx, char_idx)])
                    part = ''
                    isValid = False
                    part_start_idx = None

# Extract the first element (index 0) from each sublist using a list comprehension
first_elements = [item[0] for item in valid_parts]
sum_of_first_elements = sum(first_elements)


# EAG
# CXD
# FBH

def calculate_adjacent_values(row_data):
    adjacencies = []
    row = row_data[1]
    row_start, row_stop = row_data[2]
    if row_start != row_stop:
        row_stop += 2
    for char_idx in range(row_start, row_stop-1):
        adjacent_indices = [
                (row-1, char_idx),  # above A
                (row+1, char_idx),  # below B
                (row, char_idx-1),  # left C
                (row, char_idx+1),  # right D
                (row-1, char_idx-1),  # above-left E
                (row+1, char_idx-1),  # below-left F
                (row-1, char_idx+1),  # above-right G
                (row+1, char_idx+1),  # below-right H
            ]
        for i, j in adjacent_indices:
                # Check if the indices are within bounds
                if 0 <= i < len(schematic) and 0 <= j < len(schematic[0]):
                    adjacencies.append((i,j))
    adjacencies = list(set(adjacencies))
    for char_idx in range(row_start, row_stop-1):
        adjacencies.remove((row,char_idx))
    return adjacencies

def check_adjacent_gears(schematic, idx, char_idx):
    adjacencies = []
    adjacent_indices = [
            (idx-1, char_idx),  # above
            (idx+1, char_idx),  # below
            (idx, char_idx-1),  # left
            (idx, char_idx+1),  # right
            (idx-1, char_idx-1),  # above-left
            (idx+1, char_idx-1),  # below-left
            (idx-1, char_idx+1),  # above-right
            (idx+1, char_idx+1),  # below-right
        ]
    for i, j in adjacent_indices:
            # Check if the indices are within bounds
            if 0 <= i < len(schematic) and 0 <= j < len(schematic[0]):
                adjacencies.append((i,j))
    return adjacencies

total_ratio = 0

all_parts = parts + valid_parts
for part in all_parts:
    part.append(calculate_adjacent_values(part))
gear_list = []
for gear in gears:
    gear_list.append([gear, check_adjacent_gears(schematic,gear[0],gear[1])])
for gear in gear_list:
    matches = []
    for adjacent in gear[1]:
        for part in all_parts:
            tmp = []
            start = part[2][0]
            stop = part[2][1]
            for i in range(start, stop):
                tmp.append((part[1],i))
            if adjacent in tmp:
                matches.append(part[0])
    matches = list(set(matches))
    if len(matches) == 2:
        total_ratio += matches[0]*matches[1]
print(f"Part 1: {sum_of_first_elements}")
print(f"Part 2: {total_ratio}")

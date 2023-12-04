schematic = [
    '......%102',
    '......%101',
    '.....%100.',
    ]

parts = []
valid_parts = []
symbols = []

def find_symbols(line):
    for char in line:
        if not char.isdigit() and char != '.' and char not in symbols:
            symbols.append(char)

# EAG
# C1D
# FBH

def check_adjacent(schematic, idx, char_idx):
    isAdjacentVal = False
    adjacent_indices = [
                (idx-1, char_idx),  # above A
                (idx+1, char_idx),  # below B
                (idx, char_idx-1),  # left C
                (idx, char_idx+1),  # right D
                (idx-1, char_idx-1),  # above-left E
                (idx+1, char_idx-1),  # below-left F
                (idx-1, char_idx+1),  # above-right G
                (idx+1, char_idx+1),  # below-right H
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
        isValid = False
        for char_idx,char in enumerate(line.strip()):
            if char.isdigit() and char != '.':
                part += char
                if not isValid:
                    # check all 8 adjacent locations
                    isValid = check_adjacent(schematic, idx, char_idx)
            elif part: 
                if isValid:
                    valid_parts.append(int(part))
                else:
                    parts.append(int(part))
                part = ''
                isValid = False
            if len(line.strip()) == char_idx+1:
                if part:
                    if isValid:
                        valid_parts.append(int(part))
                    else:
                        parts.append(int(part))
                    part = ''
                    isValid = False


print(sum(valid_parts))

# 000
# 0*0
# 000
# returns all 0 locations in a list of tuples
def check_adjacent(schematic, row_idx, col_idx):
    adjacencies = []
    rows, row_size = len(schematic), len(schematic[0])

    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if 0 <= i < rows and 0 <= j < row_size and (i != row_idx or j != col_idx):
                adjacencies.append((i, j))

    return adjacencies

# ......
# .123..
# ......
# returns the locations of a part like so [(1,1),(1,2),(1,3)]
def check_locations(row_idx, start_idx, row_stop_idx):
    locations = []
    for i in range(start_idx, row_stop_idx+1):
        locations.append((row_idx,i))
    return locations

parts = []
gears = [] # list of each gears adjacencies since we don't need to remember actual gear
           # location just where it is touching

with open('gear_input.txt', 'r') as file:
    schematic = file.readlines()
    for idx,line in enumerate(schematic):
        part = ''
        row_start_idx = None
        for char_idx,char in enumerate(line):
            if char == '*':
                gear_adjacencies = check_adjacent(schematic, idx, char_idx)
                gears.append(gear_adjacencies)
            if char.isdigit() and char != '.':
                if row_start_idx == None:
                    row_start_idx = char_idx
                part += char
            elif part:
                if char_idx == len(line) - 1 or not char.isdigit():
                    parts.append([int(part), check_locations(idx, row_start_idx, char_idx - 1)])
                    part = ''
                    row_start_idx = None

sum_gear_ratio = 0
# for each gear we find any part in which the gears adjacency point 
# intersects with a part number location and add it to a set, if the set has only two
# matches we will add the product of it to our total gear ratio
for gear in gears:
    unique_matches = set()
    for part in parts:
        if any(location in gear for location in part[1]):
            unique_matches.add(part[0])
    if len(unique_matches) == 2:
        sum_gear_ratio += unique_matches.pop() * unique_matches.pop()


print(sum_gear_ratio)
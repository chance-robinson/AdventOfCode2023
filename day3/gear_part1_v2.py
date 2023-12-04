symbols = []

# finds all unique symbols in the 'schematic'
def find_symbols(line):
    for char in line:
        if not char.isdigit() and char != '.' and char not in symbols:
            symbols.append(char)

# bAAAc
# B617C
# bDDDc
# returns True if any point adjacent to a part is a symbol else False
def check_adjacent(schematic, row_idx, start_idx, row_stop_idx):
    def check_left(row, row_idx): # Bb
        if row_idx-1 >= 0:
            if schematic[row][row_idx-1] in symbols:
                return True
    def check_right(row, row_idx): # Cc
        if row_idx+1 <= row_size:
            if schematic[row][row_idx+1] in symbols:
                return True
        
    rows = len(schematic)
    row_size = len(schematic[0])
    #check all top: bAAAc
    if row_idx-1 >= 0:
        top_left = check_left(row_idx-1,start_idx) # b
        top_right = check_right(row_idx-1,row_stop_idx) # c
        if top_left or top_right:
            return True
        for i in range(start_idx, row_stop_idx+1): # AAA
            if schematic[row_idx-1][i] in symbols:
                return True
    #check bottom: bDDDc
    if row_idx+1 < rows:
        bottom_left = check_left(row_idx+1,start_idx) # b
        bottom_right = check_right(row_idx+1,row_stop_idx) # c
        if bottom_left or bottom_right:
            return True
        for i in range(start_idx, row_stop_idx+1): # DDD
            if schematic[row_idx+1][i] in symbols:
                return True

    #check middle left: B
    left = check_left(row_idx,start_idx)
    # #check middle right: C
    right = check_right(row_idx,row_stop_idx)
    if left or right:
        return True
    return False

sum = 0
with open('gear_input.txt', 'r') as file:
    schematic = file.readlines()
    for line in schematic:
        find_symbols(line.strip())
    # going through schematic line by line and forming each part by checking for digits
    for idx,line in enumerate(schematic):
        part = ''
        row_start_idx = None
        for char_idx,char in enumerate(line):
            if char.isdigit() and char != '.':
                if row_start_idx == None:
                    row_start_idx = char_idx
                part += char
            elif part:
                if char_idx == len(line) - 1 or not char.isdigit():
                    if check_adjacent(schematic, idx, row_start_idx, char_idx - 1):
                        sum += int(part)
                    part = ''
                    row_start_idx = None

print(sum)
# function will take in a partial string with a direction and find the
# substrings for each digit from a line of characters
def partialParseCharToDigit(partial_line, direction):
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    digit_positions = []
    for word, digit in digit_mapping.items():
        start_index = 0
        while start_index < len(partial_line):
            index = partial_line.find(word, start_index)
            if index == -1:
                break
            digit_positions.append((digit, index))
            start_index = index + 1
    digit_positions = sorted(digit_positions, key=lambda x: x[1])
    if (direction == 'left' and digit_positions):
        return digit_positions[0][0]
    if (direction == 'right' and digit_positions):
        return digit_positions[-1][0]
    return ''


# write function that takes a string in from the list of strings
# that combines the first digit and last digit from the passed in string
def calculateCalibrationValue(line):
    left_val, right_val = '', ''
    stop_idx = 0
    for char in line:
        stop_idx += 1
        if char.isdigit():
            left_val = char
            new_val = partialParseCharToDigit(line[0:stop_idx-1], 'left')
            if new_val:
                left_val = new_val
            break
    stop_idx = -1
    for char in reversed(line):
        stop_idx -= 1
        if char.isdigit():
            right_val = char
            new_val = partialParseCharToDigit(line[-1:stop_idx+1:-1][::-1], 'right')
            if new_val:
                right_val = new_val
            break
    if left_val == '' and right_val == '':
        left_val = partialParseCharToDigit(line, 'left')
        right_val = partialParseCharToDigit(line, 'right')

    calibrationValue = int(left_val + right_val)
    return calibrationValue

# read in our input and pass it into an array
lines = []
with open('trebuchet_input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# we will use the function for each string in the array to get the total sum
sum = 0
for line in lines:
    sum += calculateCalibrationValue(line)

print(sum)
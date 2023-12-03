# write function that takes a string in from the list of strings
# that combines the first digit and last digit from the passed in string
def calculateCalibrationValue(line):
    left_val, right_val = '', ''
    for char in line:
        if char.isdigit():
            left_val = char
            break
    for char in reversed(line):
        if char.isdigit():
            right_val = char
            break

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
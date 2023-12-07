# We are solving for the highest and lowest values for the equation:
# Best_Distance < (New_Distance)
# Best_Distance < ((Time_Given - Time_Holding_Button) * (1 Millimeter acceleration * Time_Holding_Button))
# If we let D = Best_Distance, t = Time_Given, and x = Time_Holding_Button and we can drop the 
# 1 Millimeter acceleration then simplify it to:
# D < (t-x)*x
# and since we always want our time to be greater than or equal to 0
# we can then express this as the quadratic inequality:
# x^2 - tx + D < 0
# Now, we'll turn this into a quadratic inequality to find the upper and lower bounds.
# Let a = 1, b = -t, c = D, and then after applying it to the quadratic formula, 
# we can simplify it as:
#     t ± sqrt(t**2 - (4 * D)) 
# x = -------------------------
#              2

import math

class Boats:
    def __init__(self, input_string):
        input_lines = input_string.strip().split('\n')
        self.times = [int(value) for value in input_lines[0].split()[1:]]
        self.best_distances = [int(value) for value in input_lines[1].split()[1:]]

    def quadratic_formula_simplified(self, t, D):
        root1 = math.floor((t + math.sqrt((t**2 - (4*D))))/2)
        root2 = math.ceil((t - math.sqrt((t**2 - (4*D))))/2)
        return root1, root2

    def part1(self):
        all_ways_win = []

        for time, best_distance in zip(self.times, self.best_distances):
            winning_distance = best_distance+1 # We want to go farther than the best distance so we add +1
            root1, root2 = self.quadratic_formula_simplified(time, winning_distance)
            ways_win = abs(root1 - root2)+1 # Add 1 to count the proper length
            all_ways_win.append(ways_win)

        return math.prod(all_ways_win)

    def part2(self):
        time = int(''.join(map(str, self.times)))
        winning_distance = int(''.join(map(str, self.best_distances)))+1

        root1, root2 = self.quadratic_formula_simplified(time, winning_distance)
        ways_win = abs(root1 - root2)+1

        return ways_win

if __name__ == "__main__":
    input_string = """
    Time:        34     90     89     86
    Distance:   204   1713   1210   1780
    """

    boats = Boats(input_string)
    result_part1 = boats.part1()
    result_part2 = boats.part2()

    print(f'Part 1: {result_part1}')
    print(f'Part 2: {result_part2}')
import copy

class GalaxyDistanceCalculator:
    """Class to calculate distances between points in a galaxy."""

    def __init__(self, input_string):
        """Initialize the GalaxyDistanceCalculator object."""
        self.galaxy_locs_init = []
        
        cosmos_lines = [list(line.strip()) for line in input_string.strip().split('\n')]
        # This for loop gives us starting location of each galaxy initially
        for i, cosmos in enumerate(cosmos_lines):
            for j, char in enumerate(cosmos):
                if char == '#':
                    self.galaxy_locs_init.append((i, j))

        # This allows us to see which rows we need to expand by checking for all empty's
        self.rows_expand = []
        for i,row in enumerate(cosmos_lines):
            if '#' not in ''.join(row):
                self.rows_expand.append(i)
        # Same thing but for columns
        self.cols_expand = []
        for j in range(len(cosmos_lines[0])):
            if '#' not in [cosmos[j] for cosmos in cosmos_lines]:
                self.cols_expand.append(j)

        print(f'Rows to expand: {self.rows_expand}')
        print(f'Columns to expand: {self.cols_expand}')

    def new_loc_values(self, X):
        """Calculate new locations based on expansion rules."""
        new_locs_init = copy.deepcopy(self.galaxy_locs_init) # Deep copy of our locations so we don't ever change the values
        # For each location we will find its new one after X amount of expansions
        for i, loc in enumerate(new_locs_init):
            cur_loc = loc
            # Update our location by each row/column and increase it if there are more points to expand
            for j in self.rows_expand:
                if loc[0] > j:
                    cur_loc = (cur_loc[0] + X - 1, cur_loc[1])
                    new_locs_init[i] = cur_loc
            for j in self.cols_expand:
                if loc[1] > j:
                    cur_loc = (cur_loc[0], cur_loc[1] + X - 1)
                    new_locs_init[i] = cur_loc
        return new_locs_init

    @staticmethod
    def manhattan_sum(locations):
        """Calculate the sum of Manhattan distances between Galaxy locations."""
        distances = []
        for start_location in locations:
            for target_location in locations:
                if start_location != target_location:
                    distance = abs(start_location[0] - target_location[0]) + abs(start_location[1] - target_location[1]) # Manhattan distance over euclidean because of 'grid'
                    distances.append(distance)
                    #print(f'From: {start_location} to: {target_location} is a manhattan distance of {distance}')
        #print(f'Sum of all distances: {sum(distances)}')
        # Dividing by 2 on the return sum because we find the shortest distance from each point even if we already have the shortest from the opposite end
        return sum(distances) // 2
    
    def solve(self, X):
        """Solve for the expansion of the cosmic galaxy by X times and return manhattan sum of points."""
        print(f'Our initial galaxy locations: {self.galaxy_locs_init}')
        locs = self.new_loc_values(X)
        print(f'Our galaxy after {X} expansions: {locs}')
        result = self.manhattan_sum(locs)
        return result
        

if __name__ == "__main__":
    # input_string = """
    # ...#......
    # .......#..
    # #.........
    # ..........
    # ......#...
    # .#........
    # .........#
    # ..........
    # .......#..
    # #...#.....
    # """

    with open('cosmic_input.txt', 'r') as file:
        input_string = file.read()

    galaxy_calculator = GalaxyDistanceCalculator(input_string)
    print(f'Part 1: {galaxy_calculator.solve(2)}')
    print('\n')
    print(f'Part 2: {galaxy_calculator.solve(1_000_000)}')

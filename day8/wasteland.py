from math import lcm
from functools import reduce
import re

class Wasteland:
    """Class to represent the Wasteland scenario and calculate steps."""

    def __init__(self, input_string):
        """Initialize the Wasteland object."""
        self.nodes = {}
        self.directions = ""
    
        sections = re.split(r'\n\s*\n', input_string.strip())
        self.directions = sections[0].strip()

        for section in sections[1:]:
            lines = section.strip().split('\n')
            for line in lines:
                key, values_str = re.match(r'(\w+)\s*=\s*\(([^)]+)\)', line).groups()
                values = tuple(value.strip() for value in values_str.split(','))
                self.nodes[key] = values

    def calculate_steps_list(self,start_list, stop_on):
        """Calculate the steps for each starting location to reach the stop on point."""
        len_directions = len(self.directions)

        steps_list = []
        for start_location in start_list:
            index = 0
            num_steps = 0
            cur_location = start_location
            while not cur_location.endswith(stop_on):
                if self.directions[index] == "L":
                    cur_location = self.nodes[cur_location][0]
                else:
                    cur_location = self.nodes[cur_location][1]
                num_steps += 1
                index = (index + 1) % len_directions
            steps_list.append(num_steps)
        
        return steps_list

    def part1(self):
        """Execute part 1 for the Wasteland object"""
        start = ['AAA']
        stop_on = 'ZZZ'
        num_steps = self.calculate_steps_list(start, stop_on)
        return num_steps[0]

    def part2(self):
        """Execute part 2 for the Wasteland object"""
        start_locations = [key for key in self.nodes.keys() if key.endswith('A')]
        stop_on = 'Z'
        steps_list = self.calculate_steps_list(start_locations, stop_on)

        lcm_result = reduce(lcm, steps_list)
        return lcm_result


if __name__ == "__main__":
    with open('wasteland_input.txt', 'r') as file:
        input_string = file.read()

    wasteland = Wasteland(input_string)
    part1_result = wasteland.part1()
    part2_result = wasteland.part2()

    print(f'Part 1: {part1_result}')
    print(f'Part 2: {part2_result}')

class MirageSumCalculator:
    """Class to extrapolate sums based on input lines."""

    def __init__(self, input_text):
        """Initialize the MirageSumCalculator object."""
        self.histories = input_text.strip().split('\n')

    def _calculate_predictions(self, history, reverse_order):
        """Calculate predictions based on the given line."""
        # Parse the line into a list of integers, if reverse_order = True then in reverse
        history_formatted = [int(value) for value in history.split()][::-1] if reverse_order else [int(value) for value in history.split()]
        history_diffs = [history_formatted]

        # Continue in while loop until each value in differences is equal to 0
        while True:
            # Find the differences between each value in the latest list in history_diffs and append it to itself
            differences = [history_diffs[-1][i + 1] - history_diffs[-1][i] for i in range(len(history_diffs[-1]) - 1)]
            history_diffs.append(differences)

            if all(diff == 0 for diff in differences):
                break
        
        # Initialize our predictions list with 0 because we know that will always be the first value
        predictions_history_diffs = [0]
        # Work out the next predicted_value in each history_diffs item from the bottom up using
        # previously predicted value
        for i in range(1, len(history_diffs)):
            predicted_value = history_diffs[-i-1][-1] + predictions_history_diffs[i - 1]
            predictions_history_diffs.append(int(predicted_value))

        return predictions_history_diffs[-1]

    def extrapolate_sum(self, reverse_order):
        """Extrapolate the sum of predictions based on input lines."""
        total_sum = 0
        for history in self.histories:
            total_sum += self._calculate_predictions(history, reverse_order)

        return total_sum
    
    def part_1(self):
        """Return the value for Part 1."""
        return self.extrapolate_sum(reverse_order=False)
    
    def part_2(self):
        """Return the value for Part 2."""
        return self.extrapolate_sum(reverse_order=True)

if __name__ == "__main__":
    with open('mirage_input.txt', 'r') as file:
        input_text = file.read()

    mirage_calculator = MirageSumCalculator(input_text)
    sum_part1 = mirage_calculator.part_1()
    sum_part2 = mirage_calculator.part_2()

    print(f'Sum for Part 1: {sum_part1}')
    print(f'Sum for Part 2: {sum_part2}')

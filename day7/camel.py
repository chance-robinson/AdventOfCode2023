class CamelGame:
    """Class to represent the Camel game and calculate sums."""

    def __init__(self, input_string):
        """Initialize the CamelGame object."""
        self.hands = []
        self.strength_order_p1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        self.strength_order_p2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        
        # Parsing input_string in immediately to our self.hands so we don't need to store in class
        input_lines = input_string.strip().split('\n')
        for line in input_lines:
            hand, bid = line.strip().split(' ')
            occurrences = {char: hand.count(char) for char in set(hand)}
            sorted_occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
            hand_obj = {'hand': hand, 'bid': bid, 'occurrences': sorted_occurrences}
            self.hands.append(hand_obj)


    def sort_types(self, strength, part):
        """Sort hand types based on strength and part."""
        types = {'five_kind': [], 'four_kind': [], 'full_house': [], 'three_kind': [], 'two_pair': [],
                 'one_pair': [], 'high_card': []}
        FIVE_KIND = 5
        FOUR_KIND = 4
        THREE_KIND = 3
        PAIR = 2

        for hand_obj in self.hands:
            hand,bid = hand_obj['hand'],hand_obj['bid']

            # If part 2 and we have J's then modify based on conditions
            if part == 2 and 'J' in hand_obj['occurrences']:
                occurrences_J = hand_obj['occurrences'].pop('J')
                if not hand_obj['occurrences']:
                    hand_obj['occurrences']['A'] = occurrences_J
                else:
                    first_key = next(iter(hand_obj['occurrences']))
                    hand_obj['occurrences'][first_key] += occurrences_J

            # Check hand type
            occurrences_values = list(hand_obj['occurrences'].values())
            if occurrences_values[0] == FIVE_KIND:
                types['five_kind'].append((hand, bid))
            elif occurrences_values[0] == FOUR_KIND:
                types['four_kind'].append((hand, bid))
            elif occurrences_values[0] == THREE_KIND:
                types['full_house' if occurrences_values[1] == PAIR else 'three_kind'].append((hand, bid))
            elif occurrences_values[0] == PAIR:
                types['two_pair' if occurrences_values[1] == PAIR else 'one_pair'].append((hand, bid))
            else:
                types['high_card'].append((hand, bid))

        # Sort hands within each type based on strength, lower index = best
        for hand_type in types:
            types[hand_type] = sorted(types[hand_type], key=lambda x: [strength.index(char) for char in x[0]])
        
        return types
    

    def calculate_sum_types(self, types):
        """Calculate the sum of bids for each hand type."""
        combined_list = []

        # Only saving bids to list in order from five_kind to high_card
        for hand_type in types.values():
            for _,bid in hand_type:
                combined_list.append(bid)

        total_sum = 0
        combined_list.reverse() # We reverse it so we can multiply value by proper index since the best value should be the highest, highest index = best

        for index, value in enumerate(combined_list):
            total_sum += int(value) * (index+1) # Add +1 to index since rank starts at 1 and not 0

        return total_sum
    
    def part1(self):
        """Execute part 1 of the Camel game."""
        types_dict = self.sort_types(self.strength_order_p1, 1)
        total_sum = self.calculate_sum_types(types_dict)
        return total_sum

    def part2(self):
        """Execute part 2 of the Camel game."""
        types_dict = self.sort_types(self.strength_order_p2, 2)
        total_sum = self.calculate_sum_types(types_dict)
        return total_sum

if __name__ == "__main__":
    with open('camel_input.txt', 'r') as file:
        input_string =  file.read()

    camel_game = CamelGame(input_string)
    part1_sum = camel_game.part1()
    part2_sum = camel_game.part2()

    print(f'Part 1: {part1_sum}')
    print(f'Part 2: {part2_sum}')

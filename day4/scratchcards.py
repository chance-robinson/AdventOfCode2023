import re

# Processing matches
sum_points = 0
total_scratchcards = []

with open('scratchcards_input.txt', 'r') as file:
    # Card   1:  5 37 | 97 17
    # This regex pattern captures 3 things:
    # 1. (\d+): Capture one or more digits and store them in a group.
    # 2. (.+?): Capture one or more of any character (non-greedy) and store in a group.
    # 3. (.+): Capture one or more of any character and store in a group.
    pattern = re.compile(r"Card\s+(\d+):(.+?)\|(.+)")
    input_string = file.read()
    scratchoffs = pattern.findall(input_string)
    
    total_scratchcards = [{'card': int(card[0]), 'occurrences': 1} for card in scratchoffs]

    for idx,card in enumerate(scratchoffs):
        winning_nums = card[1].split()
        our_nums = card[2].split()
        # & is the set intersection operator not bitwise AND when used between sets
        num_card_common = len(set(winning_nums) & set(our_nums))
        
        # for 1st one we want it to be one then doubled so on, that is
        # why we subtract 1 from the amount of nums we have be cause
        # 2**0 is 1
        card_points = 2**(num_card_common-1) if num_card_common > 0 else 0
        sum_points += card_points

        # Update occurrences for subsequent cards
        # our cards start at 1 but out index starts at 0, so we add 1
        current_card_num = idx+1
        for j in range(current_card_num, current_card_num+num_card_common):
            total_scratchcards[j]['occurrences'] += 1 * total_scratchcards[idx]['occurrences']

# Sum up all occurrences in num_copies
total_occurrences = sum(card['occurrences'] for card in total_scratchcards)

print(f'Part 1: {sum_points}')
print(f'Part 2: {total_occurrences}')
# games_list = [
#     'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# ]
games_list = []

sum_ids = 0
game_color_max = {'red': 12, 'green': 13, 'blue': 14}
sum_powersets = 0

# for game in games_list:
with open('cube_input.txt', 'r') as file:
    for game in file:
        cur_power_game = 1
        cur_game_max = {'red': 0, 'green': 0, 'blue': 0}
        game_number, pulls = game.split(':', 1)
        game_number = int(game_number.strip().replace('Game ', ''))
        pulls = pulls.split(';')
        for pull in pulls:
            pairs = pull.strip().split(',')
            for pair in pairs:
                num_Cubes, color_Cube = pair.strip().split(' ')
                num_Cubes = int(num_Cubes)
                if cur_game_max[color_Cube] < num_Cubes:
                    cur_game_max[color_Cube] = num_Cubes
        comparison_result = any(cur_game_max[color_Cube] > game_color_max[color_Cube] for color_Cube in cur_game_max)
        if not comparison_result:
            sum_ids += game_number
        for color_Cube in cur_game_max:
             cur_power_game *= cur_game_max[color_Cube]
        sum_powersets += cur_power_game

print('Day 2 of the Advent Of Code 2023')
print(f'Puzzle 1: {sum_ids}')
print(f'Puzzle 2: {sum_powersets}')
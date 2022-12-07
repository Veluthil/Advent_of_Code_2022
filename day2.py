with open("inputs/input-day2.txt") as f:
    data = [line.strip().replace(' ', '') for line in f]

    first_dict = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
    second_dict = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}

    part_one = sum(first_dict[round] for round in data)
    part_two = sum(second_dict[round] for round in data)


print(f'Answer for Part One: {part_one}.')
print(f'Answer for Part Two: {part_two}.')
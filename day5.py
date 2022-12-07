from copy import deepcopy


def part_one(crates, moves):
    for number, start, end in moves:
        for crate in range(number):
            crates[end-1].append((crates[start-1]).pop())
    return "".join([x.pop() for x in crates])


def part_two(crates, moves):
    for number, start, end in moves:
        crates[end-1].extend(crates[start-1][-number:])
        crates[start-1] = crates[start-1][:-number]
    return "".join([x.pop() for x in crates])


with open("inputs/input-day5.txt") as f:
    crates, moves = f.read().split('\n\n')
    moves = [[int(x) for x in x.split() if x.isdigit()] for x in moves.splitlines()]
    crates_reformed = [
        ['H', 'T', 'Z', 'D'],
        ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
        ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
        ['L', 'C', 'N', 'F', 'H', 'Z'],
        ['G', 'L', 'F', 'Q', 'S'],
        ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
        ['Z', 'F', 'J'],
        ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],
        ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']
    ]

    print(f"Answer for PART ONE: {part_one(deepcopy(crates_reformed), moves)}.")
    print(f"Answer for PART TWO: {part_two(deepcopy(crates_reformed), moves)}.")

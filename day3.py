with open("inputs/input-day3.txt") as f:
    data = f.read().split('\n')

# ---- PART ONE ------
    sum_of_items_value = 0

    for rucksack in data:
        compartment1 = slice(0, len(rucksack) // 2)
        compartment2 = slice(len(rucksack) // 2, len(rucksack))
        # print(rucksack[compartment1], rucksack[compartment2])
        items = list(set(rucksack[compartment1]) & set(rucksack[compartment2]))
        for item in items:
            common_item = item
        number = ord(common_item) - 96
        if number < 0:
            number += 58
        sum_of_items_value += number

    print(f"Sum of items value in Part One: {sum_of_items_value - 33}.")


# ------ PART TWO ------
    number_of_iteration = 0
    group_of_elves = []
    sum_of_badges_value = 0

    for rucksack in data[number_of_iteration:]:
        group_of_elves.append(rucksack)
        # print(group_of_elves)
        if len(group_of_elves) == 3:
            common = set.intersection(*map(set, group_of_elves))
            for item in common:
                common_item = item
                # print(common_item)
            number = ord(common_item) - 96
            if number < 0:
                number += 58
            sum_of_badges_value += number
            group_of_elves.clear()
            number_of_iteration += 3

    print(f"Sum of budges value in Part Two: {sum_of_badges_value}.")

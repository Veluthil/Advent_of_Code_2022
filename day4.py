with open("inputs/input-day4.txt") as f:
    data = f.read().split('\n')

    overlapping_groups = 0
    any_overlaps = 0

    for pair in data:
        split_pair = pair.split(',')
        pair1 = split_pair[0].split('-')
        pair2 = split_pair[1].split('-')
        list1 = []
        list2 = []
        for number in range(int(pair1[0]), int(pair1[1]) + 1):
            list1.append(number)
        for number in range(int(pair2[0]), int(pair2[1]) + 1):
            list2.append(number)
        check1 = all(item in list1 for item in list2)
        check2 = all(item in list2 for item in list1)
        if check1:
            overlapping_groups += 1
        elif check2:
            overlapping_groups += 1
        overlap = any(item in list1 for item in list2)
        if overlap:
            any_overlaps += 1

    print(f"Count of full overlaps in groups for PART ONE: {overlapping_groups}.")
    print(f"Any occurring overlaps for PART TWO: {any_overlaps}.")

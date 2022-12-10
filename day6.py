# ---- PART ONE ----
fours = []
with open('inputs/input-day6.txt') as f:
    data = f.read()
    for char in data:
        fours.append(char)
        if len(fours) > 4:
            set_of_four = set(fours[-5:-1])
            if len(set_of_four) == 4:
                print(f"Number of characters needed to process in PART ONE: {len(fours) - 1}.")
                # print(set_of_four)
                break


# ---- PART TWO ----
fourteens = []
with open('inputs/input-day6.txt') as f:
    data = f.read()
    for char in data:
        fourteens.append(char)
        if len(fourteens) > 14:
            set_of_fourteen = set(fourteens[-15:-1])
            if len(set_of_fourteen) == 14:
                print(f"Number of characters needed to process in PART TWO: {len(fourteens) - 1}.")
                # print(set_of_fourteen)
                break

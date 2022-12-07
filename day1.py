new_list = []
elfs_calories = 0

with open('inputs/input-day1.txt') as f:
    data = f.read().split('\n')

    for number in data:
        if number != '':
            elfs_calories += int(number)
        else:
            new_list.append(elfs_calories)
            elfs_calories = 0

# ---- PART ONE ----
print(f"Elf with the most Calories carries: {max(new_list)} Calories.")

# ---- PART TWO ----
new_list.sort()
elf1 = (new_list[-1])
elf2 = (new_list[-2])
elf3 = (new_list[-3])
print(f"Top three Elves carry: {elf3 + elf2 + elf1} Calories in total.")


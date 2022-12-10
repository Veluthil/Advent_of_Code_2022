x = 1
rounds = 0
strength_sum = 0
signal = []


def ticking():
    global rounds, strength_sum
    rounds += 1
    if rounds in (20, 60, 100, 140, 180, 220):
        strength_sum += (x * rounds)


# ------------ PART ONE ------------

with open("inputs/input-day10.txt") as f:
    data = f.read().split('\n')
    for step in data:
        split_step = step.split(" ")
        if split_step[0] == "noop":
            ticking()
            signal.append(x)
        elif split_step[0] == "addx":
            ticking()
            ticking()
            signal.extend([x, x])
            x += int(split_step[1])

    print(f"Strength sum for Part One: {strength_sum}.")

    # ------------- PART TWO ----------------

    print("Message in Part Two:")

    for y in range(6):
        CRT_line = ''
        for x in range(40):
            cycle = x + (y * 40)
            CRT_line += '##' if abs(x - signal[cycle]) <= 1 else '  '

        print(CRT_line)

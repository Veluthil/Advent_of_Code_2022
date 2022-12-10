# # ----- PART ONE -----
#
#     visible_trees = 0
#     for tree_x in range(x):
#         for tree_y in range(y):
#             if check(forest, tree_x, tree_y):
#                 visible_trees += 1
#     print(visible_trees)
#
# def visibility(grid, x, y, coords, horizontal):
#     size = len(grid)
#     if x in (0, size - 1) or y in (0, size - 1):
#         return True, 0 # at the edge the scenic score is 0
#     visible = True
#     score = 0
#     for coord in coords:
#         score += 1
#         if (grid[y][coord] if horizontal else grid[coord][x]) >= grid[y][x]:
#             visible = False
#             break
#     return visible, score
#
# with open("inputs/input-day8.txt") as file:
#     grid = [[int(tree) for tree in row.strip()] for row in file]
#     size = len(grid) # assume the grid is a squre
#     visibilities = {}
#     scenic_scores = {}
#     for y in range(size):
#         for x in range(size):
#             coords = range(x - 1, -1, -1), range(x + 1, size), range(y - 1, -1, -1), range(y + 1, size)
#             directions = True, True, False, False
#             for coords, dir in zip(coords, directions):
#                 visible, score = visibility(grid, x, y, coords, dir)
#                 if not visibilities.get((x, y), False): # if True already found, don't change
#                     visibilities[x, y] = visible
#                 scenic_scores[x, y] = scenic_scores.get((x, y), 1) * score
#     print(sum(visibilities.values()))
#     print(max(scenic_scores.values()))
# -------------------------------------------------------------------
# --------------- PART ONE FUNCTIONS --------------
def part_one():
    check_top()
    check_bottom()
    check_left()
    check_right()
    return len(visible_trees_count)


def check_top():
    for col in range(len(array[0])):
        visible_tree = -1
        for row in range(len(array)):
            possible_tree = int(array[row][col])
            if possible_tree > visible_tree:
                visible_tree = possible_tree
                tree_coordinates = (row, col)
                visible_trees_count.add(tree_coordinates)


def check_bottom():
    for col in range(len(array[0])):
        visible_tree = -1
        for row in range(len(array)):
            possible_tree = int(array[len(array) - 1 - row][col])
            if possible_tree > visible_tree:
                visible_tree = possible_tree
                tree_coordinates = (len(array) - 1 - row, col)
                visible_trees_count.add(tree_coordinates)


def check_left():
    for row in range(len(array)):
        visible_tree = -1
        for col in range(len(array[0])):
            possible_tree = int(array[row][col])
            if possible_tree > visible_tree:
                visible_tree = possible_tree
                tree_coordinates = (row, col)
                visible_trees_count.add(tree_coordinates)


def check_right():
    for row in range(len(array)):
        visible_tree = -1
        for col in range(len(array[0])):
            possible_tree = int(array[row][len(array) - 1 - col])
            if possible_tree > visible_tree:
                visible_tree = possible_tree
                tree_coordinates = (row, len(array) - 1 - col)
                visible_trees_count.add(tree_coordinates)


# --------- PART TWO FUNCTIONS --------------


def scenic_score(row_ix, column_ix):
    value = array[row_ix][column_ix]
    row = array[row_ix]
    column = [array[row_ix][column_ix] for row_ix in range(len(array))]

    left, right, top, bottom = 0, 0, 0, 0

    # Check left
    for x in reversed(row[:column_ix]):
        left += 1
        if x >= value:
            break

    # Check right
    for x in row[column_ix + 1:]:
        right += 1
        if x >= value:
            break

    # Check top
    for x in reversed(column[:row_ix]):
        top += 1
        if x >= value:
            break

    # Check bottom
    for x in column[row_ix + 1:]:
        bottom += 1
        if x >= value:
            break

    return left * right * top * bottom


# ---------- SOLUTIONS ----------------
with open("inputs/input-day8.txt") as f:
    forest = f.read().split('\n')
    array = [[int(tree) for tree in grid] for grid in forest]

# ------ PART ONE -------
    visible_trees_count = set()
    print(f"Sum of visible trees from edges is: {part_one()}.")

# ------- PART TWO --------
    highest_scenic_score = max([scenic_score(row_ix, column_ix)
                                for row_ix in range(len(array))
                                for column_ix in range(len(array[row_ix]))])
    print(f"Highest scenic score is equal to: {highest_scenic_score}.")




#-------------------------------------------------------
# import numpy as np
#
#
# def part_one():
#     array = np.genfromtxt("inputs/input-day8.txt", delimiter=1)
#     visible_trees = np.empty(array.shape, dtype=str)
#     for _ in range(0, 4):
#         for x, grid in enumerate(array):
#             highest_tree = -1
#             for y, tree in enumerate(grid):
#                 if tree > highest_tree:
#                     highest_tree = tree
#                     visible_trees[x, y] = "x"
#         array = np.rot90(array)
#         visible_trees = np.rot90(visible_trees)
#     return np.count_nonzero(visible_trees == 'x')
#
#
# def part_two():
#     array = np.genfromtxt("inputs/input-day8.txt", delimiter=1)
#     scenic_score = np.empty(array.shape)
#     for x, grid in enumerate(array):
#         for y, tree in enumerate(grid):
#             up = calculate_sight(tree, np.flip(array[:x, y]))
#             down = calculate_sight(tree, array[x + 1:, y])
#             left = calculate_sight(tree, np.flip(grid[:y]))
#             right = calculate_sight(tree, grid[y+1:])
#             score = up * left * down * right
#             scenic_score[x, y] = score
#     return np.max(scenic_score)
#
#
# def calculate_sight(value, trees):
#     sight = 1
#     if not np.size(trees):
#         return 0
#     for tree in trees:
#         if value > tree:
#             sight += 1
#         else:
#             return min(len(trees), sight)
#     return min(len(trees), sight)
#
#
# print(part_one())
# print(int(part_two()))

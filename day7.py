with open("inputs/input-day7.txt", mode='r', encoding='utf8') as f:

    directories = []
    size_of_dir = {}

    data = f.readlines()
    for line in data:
        commands_and_files = line.split()
        if commands_and_files[0] == '$':
            if commands_and_files[1] == 'cd' and commands_and_files[2] == '..':
                directories = directories[:-1]
            elif commands_and_files[1] == 'cd' and commands_and_files[2] != '..':
                directories.append(commands_and_files[2])
                size_of_dir['/'.join(directories)] = 0
        elif commands_and_files[0].isdigit():
            copy_of_dir = directories.copy()
            while len(copy_of_dir) > 0:
                size_of_dir['/'.join(copy_of_dir)] += int(commands_and_files[0])
                copy_of_dir.pop()


# ---- PART ONE ----
# print(size_of_dir)
child_dir = {file: size for (file, size) in size_of_dir.items() if size <= 100000}
# print(child_dir)
print(f"Sum of the total sizes of directories with size at most 100 000: {sum(child_dir.values())}")

# ---- PART TWO ----
initial_size = sum(size_of_dir.values())
free_space = 70000000 - size_of_dir.get('/')
print(f"Total size of files in all directories: {initial_size}")
min_required_to_delete = 30000000 - free_space
directory_to_delete = (min(size for file, size in size_of_dir.items() if size >= min_required_to_delete))
print(f"Smallest directory to delete has size of: {directory_to_delete}")

test = False
infty = float('inf')
data = open("2025_7_input.txt")
if test:
    data = open("2025_7_test.txt")


grid = data.readlines()
for i in range(len(grid)):
    grid[i] = grid[i].strip()

row_len = len(grid[0])
cur_row = [0] * row_len
stack = []
for i, space in enumerate(grid[0]):
    if space == 'S':
        cur_row[i] = 1
        stack.append([0, i])
        break
split_count = 0
time_lines = 1

for i, row in enumerate(grid[1:]):
    next_row = [0] * row_len

    for j, space in enumerate(cur_row):
        if space > 0:
            if row[j] == '.':
                next_row[j] += cur_row[j]
            elif row[j] == '^':
                split_count += 1
                time_lines -= 1
                if j > 0:
                    next_row[j-1] += cur_row[j]
                    time_lines += 1
                if j < row_len-1:
                    next_row[j+1] += cur_row[j]
                    time_lines += 1
    cur_row = next_row


print(split_count)
print(sum(cur_row))


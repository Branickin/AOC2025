import time

input = open("2025_4_input.txt")
# input = open("2025_4_test.txt")

grid = [s.strip() for s in input]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
height = len(grid)
width = len(grid[0])
counts = []


def countAdj(i,j):
    count = 0
    if grid[i][j] == '.':
        return -1
    for d in directions:
        newi = d[0]+i
        newj = d[1]+j
        if newi < 0 or newj < 0 or newi >= height or newj >= width:
            continue
        if grid[newi][newj] == '@':
            count += 1
    return count

def solve_part1():
    total = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '@' and countAdj(i, j) < 4:
                total += 1
    return total


def remove_roll(i,j):
    counts[i][j] = -1
    total = 0
    for d in directions:
        newi = d[0] + i
        newj = d[1] + j
        if newi < 0 or newj < 0 or newi >= height or newj >= width:
            continue
        if counts[newi][newj] >= 0:
            counts[newi][newj] -= 1
            if 0 <= counts[newi][newj] < 4:
                total += remove_roll(newi, newj)
    return total +1



def solve_part2():
    for i in range(height):
        r = []
        for j in range(width):
            r.append(countAdj(i, j))
        counts.append(r)
    total = 0
    for i in range(height):
        for j in range(width):
            if 0 <= counts[i][j] < 4:
                total += remove_roll(i,j)
    return total

print(solve_part1())

print(solve_part2())


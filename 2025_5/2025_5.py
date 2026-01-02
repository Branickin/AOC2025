from bisect import bisect_left
from sortedcontainers import SortedList

test = False
infty = float('inf')
data = open("2025_5_input.txt")
if test:
    data = open("2025_5_test.txt")

ranges = SortedList()

for line in data:
    if line == '\n':
        break
    left, right = map(int, line.split('-'))

    left_ind = ranges.bisect_left([left, infty])
    right_ind = ranges.bisect_left([right, infty])

    if left_ind > 0 and ranges[left_ind-1][0] <= left <= ranges[left_ind-1][1]+1:
        left_ind -= 1
    if right_ind < len(ranges) and ranges[right_ind][0]-1 <= right:
        right_ind+=1
    overlap = list(ranges.islice(left_ind, right_ind))
    if len(overlap) == 0:
        ranges.add([left, right])
        continue

    new_interval = [min(left, overlap[0][0]), max(right,  overlap[-1][1])]
    for i in reversed(range(left_ind, right_ind)):
        ranges.pop(i)
    ranges.add(new_interval)


def checkFresh(x):
    d = ranges.bisect_left([x, float("inf")])-1
    if d > len(ranges) or d < 0:
        return 0
    if ranges[d][0] <= x <= ranges[d][1]:
        return 1
    return 0


def part2(x):
    return (x[1]-x[0])+1

x = list(data.readlines())
print(sum(map(checkFresh, map(int,x))))
print(sum(map(part2, ranges)))


# Wrong 355188842412384



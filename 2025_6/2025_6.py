import math
import itertools

test = False
infty = float('inf')
data = open("2025_6_input.txt")
if test:
    data = open("2025_6_test.txt")


probs = []
part_2 = []

for row in data:
    probs.append(row.split())
    part_2.append(row.rstrip())

part_2 = part_2[0:len(part_2)-1]
mxlen = max(map(len, part_2))+1

part_2 = list(map(str.ljust, part_2, itertools.repeat(mxlen)))
print(part_2)
ops = probs[-1]

ans = 0
for i in range(len(probs[0])):
    op = probs[-1][i]
    temp = 0
    if op == '+':
        for j in range(len(probs)-1):
            temp += int(probs[j][i])
    elif op == '*':
        temp = 1
        for j in range(len(probs)-1):
            temp *= int(probs[j][i])
    ans += temp

print(ans)


def cust_int(str):
    if not str.strip():
        return 0
    return int(str)


ans2 = 0
print(part_2)
col = 0
for op in ops:
    nums = []
    while num := cust_int("".join([row[col] for row in part_2])):
        nums.append(num)
        col += 1
    col += 1
    if op == '+':
        ans2 += sum(nums)
    elif op == '*':
        ans2 += math.prod(nums)

print(ans2)


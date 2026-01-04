import time
from collections import deque
from scipy.optimize import linprog
test = False
data = open("2025_10_input.txt")
if test:
    data = open("2025_10_test.txt")

lines = data.readlines()
def part1():
    def target_generator(data):
        target = 0
        mask = 1 << len(data) - 1
        for c in data:
            if c == '#':
                target |= mask
            mask >>= 1

        return target

    def button_generator(t_len, data):
        masks = []
        for button in data:
            m = 0
            nums = button[1:-1].split(',')
            for num in nums:
                m |= (1 << (t_len - int(num)))
            masks.append(m)
        return masks

    def bfs(target, buttons):
        queue = deque()
        queue.append((0, 0))
        seen = set()
        seen.add(0)

        while queue:
            current = queue.popleft()
            for button in buttons:
                new = current[0] ^ button
                if new not in seen:
                    if new == target:
                        return current[1] + 1
                    seen.add(new)
                    queue.append((new, current[1] + 1))
        raise ValueError("Cannot reach target")

    s = time.time()
    targets = []
    buttons = []
    for line in lines:
        segments = line.split()
        targets.append(target_generator(segments[0][1:-1]))
        buttons.append(button_generator(len(segments[0][1:-1]) - 1, segments[1:-1]))
    ans = sum(map(bfs, targets, buttons))
    # print(ans)
    print(time.time() - s)

def part2():
    def target_generator(data):
        return list(map(int, data[1:-1].split(',')))

    def button_generator(data):
        return list(map(target_generator, data))

    def func(target, butts):
        A = [[0 for col in range(len(butts))] for row in range(len(target))]
        for i in range(len(butts)):
            for b in butts[i]:
                A[b][i] = 1
        c = [1]*len(butts)
        ans = linprog(c, A_eq=A,b_eq=target, method="highs", integrality=c)

        return sum(ans.x)

    s = time.time()
    targets = []
    buttons = []
    for line in lines:
        segments = line.split()
        targets.append(target_generator(segments[-1]))
        buttons.append(button_generator(segments[1:-1]))
    ans = int(sum(map(func, targets, buttons)))
    print(ans)
    print(time.time() - s)

part1()
part2()

# BFS
# 0.006350040435791016

# 0.21474361419677734

# 15101
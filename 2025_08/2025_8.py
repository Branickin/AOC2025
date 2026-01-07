from heapq import *
from math import dist
from disjointSet import DisjointSet

test = False
infty = float('inf')
data = open("2025_8_input.txt")

connections = 1000
if test:
    data = open("2025_8_test.txt")
    connections = 10
heap = []
points = list(map(lambda r: list(map(int, r.split(','))), data))

for i, p1 in enumerate(points):
    for j in range(i+1, len(points)):
        heappush(heap, [dist(p1, points[j]), i, j])


def part1(heapP1, cons):
    ds = DisjointSet(len(points))
    while cons > 0 and len(heapP1):
        _, a, b = heappop(heapP1)
        ds.setUnion(a, b)
        cons -= 1

    m1 = m2 = m3 = 1

    for x in ds.getList():
        if x < m1:
            m1, m2, m3 = x, m1, m2
        elif x < m2:
            m2, m3 = x, m2
        elif x < m3:
            m3 = x

    print(abs(m1*m2*m3))


def part2(heapP2):
    ds = DisjointSet(len(points))
    ans = 0
    while ds.size(0) != len(points):
        _, a, b = heappop(heapP2)
        ds.setUnion(a, b)
        ans = abs(points[a][0]*points[b][0])
    print(ans)


part1(heap, connections)
# part2(heap)

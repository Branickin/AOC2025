import time
from collections import deque

from anyio.functools import lru_cache

test = False
data = open("2025_11_input.txt")
if test:
    data = open("2025_11_test.txt")



def create_graph(data):
    g = {}
    ns = []
    for row in data:
        nodes = row.split()
        g[nodes[0][:-1]] = nodes[1:]
        ns.append(nodes[0][:-1])
    return g, ns

@lru_cache()
def dfs(node, dest):
    s = 0
    for n in graph[node]:
        if n == dest:
            s+=1
        elif n in graph:
            s += dfs(n, dest)
    return s

@lru_cache()
def dfs2(node, dest, ex):
    s = 0
    for n in graph[node]:
        if n == ex:
            continue
        elif n == dest:
            s+=1
        elif n in graph:
            s += dfs2(n, dest, ex)
    return s
st = time.time()
graph, nodes = create_graph(data)




# print(dfs("you", "out"))
# print(time.time() - st)
# st = time.time()
a = dfs2("svr", "dac", "fft")
b = dfs2("dac", "fft", "dac")
c = dfs2("fft", "out", "dac")
e = dfs2("svr", "fft", "dac")
f = dfs2("fft", "dac", "fft")
g = dfs2("dac", "out", "fft")
d = a*b*c
h = e*f*g

print(d+h)
print(time.time() - st)
# b = dfs("svr", "fft") + dfs("fft", "dac") + dfs("dac", "out")
# print(a + b)



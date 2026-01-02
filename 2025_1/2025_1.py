import math

f = open("2025_1_test.txt")
f2 = open("2025_1_input.txt")

count = 0
d = 50
# for l in f:
#     l = l.strip()
#
#     op = 1
#     if l[0] == 'L':
#         op = -1
#     d += (int(l[1:]) * op)
#     # if d < 0:
#     #     d += 100
#     # if d > 99:
#     #     d -= 100
#     d %= 100
#     if d == 0:
#         count+=1


# print(d)
prev_d = 50
for l in f2:
    l = l.strip()
    op = 1
    if l[0] == 'L':
        op = -1
    print(l)
    rotate_amt = (int(l[1:]))
    count += abs(rotate_amt) // 100
    rotate_amt %= 100
    prev_d = d
    d += rotate_amt * op

    if (d <= 0 or d >= 100) and prev_d != 0:
        print(l)
        count+=1

    d %= 100


print(count)
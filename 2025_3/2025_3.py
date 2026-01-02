def find_max_p1(s):
    d_1 = d_2 = 0
    s=s.strip()
    print(s)

    for i in range(len(s)):
        num = int(s[i])
        if num > d_1 and i != len(s)-1:
            d_1 = num
            d_2 = 0
        elif num > d_2:
            d_2 = num
    print(d_1,d_2)
    return d_1*10 + d_2


def find_max_p2(s, digits_left=12):
    d_1 = 0
    index = 0
    for i in range(len(s)-(digits_left-1)):
        num = int(s[i])
        if num > d_1:
            d_1 = num
            index = i
            if d_1 == 9:
                break
    if digits_left == 1:
        return d_1
    return d_1*10**(digits_left-1) + find_max_p2(s[index+1:], digits_left-1)


f = open("2025_3_input.txt")
data = list(map(str.strip, f.readlines()))
# data = ["987654321111111", "811111111111119","234234234234278" ,"818181911112111"]
# print(sum(map(find_max_p1, data)))
print(sum(map(find_max_p2, data)))
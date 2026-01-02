import time

input = "3335355312-3335478020,62597156-62638027,94888325-95016472,4653-6357,54-79,1-19,314-423,472-650," \
        "217886-298699,58843645-58909745,2799-3721,150748-178674,9084373-9176707,1744-2691,17039821-17193560," \
        "2140045-2264792,743-1030,6666577818-6666739950,22946-32222,58933-81008,714665437-714803123,9972438-10023331," \
        "120068-142180,101-120,726684-913526,7575737649-7575766026,8200-11903,81-96,540949-687222,35704-54213," \
        "991404-1009392,335082-425865,196-268,3278941-3383621,915593-991111,32-47,431725-452205"







def compare(s):
    n = len(s)
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            if s == s[:k] * (n // k):
                return True
    return False


start = time.time()

total = 0
ranges = input.split(',')
for r in ranges:
    lower, upper = map(int, r.split('-'))

    for num in range(lower, upper+1):
        if compare(str(num)):
            total += num


t = time.time()
print(total)
print(t-start)



def is_repetition(s):
    n = len(s)
    # Only check divisors of length (but not full length)
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            if s == s[:k] * (n // k):
                return True
    return False


def sum_invalid_ids(input):
    total = 0
    ranges = input.split(',')

    for r in ranges:
        lo, hi = map(int, r.split('-'))
        for num in range(lo, hi + 1):
            if is_repetition(str(num)):
                total += num

    return total


start = time.time()
print(sum_invalid_ids(input))
t = time.time()
print(t-start)
# 34459250159
# 20942028255
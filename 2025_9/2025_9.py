import itertools
import time
import shapely

test = False
data = open("2025_9_input.txt")
if test:
    data = open("2025_9_test.txt")

s = time.time()
def area(p1, p2):
    return (1+abs(p1[0]-p2[0]))*(1+abs(p1[1]-p2[1]))



x = list(map(str.split, data.readlines(), itertools.repeat(',')))

points = list(map(lambda r: [int(r[0]), int(r[1])], x))
polygon = shapely.Polygon(points)
shapely.prepare(polygon)
part_1 = 0
part_2 = 0
for i in range(len(points)):
    for j in range(i+1,len(points)):
        a = area(points[i],points[j])
        part_1 = max(a,part_1)
        if a > part_2:
            if polygon.covers(shapely.Point(points[i][0],points[j][1])) and polygon.contains(shapely.Point(points[j][0],points[i][1])):
                other_rec = shapely.Polygon([points[i],(points[i][0],points[j][1]),points[j],(points[j][0],points[i][1]) ])
                if polygon.contains(other_rec):
                    part_2 = a



print(part_1)
print(part_2)
t = time.time()
print(t-s)


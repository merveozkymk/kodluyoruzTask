import math

points = [(1, 2), (3, 4), (6, 8), (0, 1)]
distances = []

def euclideanDistance(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

minDistance = min(distances)

print("Mesafeler: ")
for i in range(len(distances)):
    print(distances[i])

print("Minimum Mesafe:", minDistance)
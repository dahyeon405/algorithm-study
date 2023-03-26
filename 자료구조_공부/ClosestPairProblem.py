import math

# reference: https://bblackscene21.tistory.com/11

# O(nlogn)

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def dist(p1, p2):
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y))

def bruteForce(P, n):
	min_val = float('inf')
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j]) < min_val:
				min_val = dist(P[i], P[j])

	return min_val

def closestSplitPair(p, Q, d):
    x = p.x
    sy = [i for i in Q if abs(i.x - x) < d]

    min_d = d
    for i in range(len(sy)):
        for j in range(1, min(7, len(sy)-i)):
            split_dist = dist(sy[i], sy[i+j])
            if dist(sy[i], sy[i+j]) < d:
                min_d = split_dist
    
    return min_d

def closestUtil(P, Q, n):
    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    min_L = closestUtil(P[:mid], Q, mid)
    min_R = closestUtil(P[mid:], Q, n-mid)
    
    min_d = min(min_L, min_R)
    min_splitPair = closestSplitPair(P[mid-1], Q, min_d)

    return min(min_d, min_splitPair)


def closestPair(points):
    n = len(points)
    P = sorted(points, key=lambda point: point.x)
    Q = sorted(points, key=lambda point: point.y)
    return closestUtil(P, Q, n)

Points = [Point(2, 3), Point(12, 30),
	Point(40, 50), Point(5, 1),
	Point(12, 10), Point(3, 4)]

print(closestPair(Points))
print(bruteForce(Points, len(Points)))
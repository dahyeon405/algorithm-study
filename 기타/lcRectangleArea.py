class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def intersectLength(a1, a2, b1, b2):
            if a2 < a1: a1, a2 = a2, a1
            if b2 < b1: b1, b2 = b2, b1
            
            if a2 <= b1 or b2 <= a1: return 0
            if a2 <= b2 and a1 >= b1: return a2-a1
            if b2 <= a2 and b1 >= a1: return b2-b1

            if a2 < b2: return a2-b1
            else: return b2-a1

        def getArea(x1, x2, y1, y2):
            x = abs(x2-x1)
            y = abs(y2-y1)
            return x*y

        a_area = getArea(ax1, ax2, ay1, ay2)
        b_area = getArea(bx1, bx2, by1, by2)
        intersect_a = intersectLength(ax1, ax2, bx1, bx2)
        intersect_b = intersectLength(ay1, ay2, by1, by2)

        print(intersect_a*intersect_b)
        return a_area + b_area - intersect_a*intersect_b
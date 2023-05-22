class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = []

        def getStckAfterCollision(stck, ast):
            if len(stck) == 0 or stck[-1]*ast > 0 or (stck[-1] < 0 and ast > 0):
                stck.append(ast)
            elif abs(stck[-1]) == abs(ast):
                stck.pop()
            elif abs(stck[-1]) < abs(ast):
                stck.pop()
                stck = getStckAfterCollision(stck, ast)
            return stck

        
        for ast in asteroids:
            stck = getStckAfterCollision(stck, ast)

        return stck

# 다른 사람의 풀이
class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
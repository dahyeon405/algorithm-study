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

# 마지막 테스트케이스에서 막히는데 Input이 없음..;;
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if matchsticks is None: return False
        _sum = sum(matchsticks)
        if _sum % 4 != 0: return False
        singleSum = _sum/4
        matchsticks.sort(reverse=True)

        visited = [False]*len(matchsticks)
        def canMakeSquare(left, curSum, idx):
            if left == 1: return True
            if curSum == singleSum: 
                return canMakeSquare(left-1, 0, 0)
            for i in range(idx, len(matchsticks)):
                if visited[i]: continue
                visited[i] = True
                if (canMakeSquare(left, curSum+matchsticks[i], i+1)): return True
                visited[i] = False
            return False

        return canMakeSquare(4, 0, 0)
# 시간 초과
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        _max = 0
        for i in range(len(hours)):
            sum = 0
            total = 0
            for k in range(i, len(hours)):
                if hours[k] > 8: sum += 1
                else: sum -= 1
                total += 1
                if sum > 0: _max = max(_max, total)

        return _max
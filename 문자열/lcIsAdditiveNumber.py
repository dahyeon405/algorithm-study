class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def _isAdditiveNum(firstNum, secondNum, idx):
            if (len(firstNum) > 1 and firstNum.startswith("0")): return False
            if (len(secondNum) > 1 and secondNum.startswith("0")): return False
            if idx >= len(num)-1: return True
            _sum = str(int(firstNum) + int(secondNum))
            if num[idx+1:].startswith(_sum):
                nextNum = num[idx+1:idx+1+len(_sum)]
                if (_isAdditiveNum(secondNum, nextNum, idx+len(_sum))): return True
            return False

        firstNum = ""
        for i in range(len(num)-1):
            firstNum += num[i]
            secondNum = ""
            for k in range(i+1, len(num)-1):
                secondNum += num[k]
                if _isAdditiveNum(firstNum, secondNum, k):
                    return True
        return False

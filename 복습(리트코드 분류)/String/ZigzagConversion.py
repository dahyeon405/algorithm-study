class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        endIdx = len(s) - 1

        if (numRows == 1): return s

        for i in range(numRows):
            if (i > endIdx): break
            result += s[i]
            nextCol = 1
            while True:   
                colIdx = (2*numRows - 2)*nextCol
                if (colIdx == 0): break
                idx = colIdx - i
                if (idx > endIdx): break
                if (i!= numRows - 1): result += s[idx]

                if (i != 0 and colIdx+i <= endIdx):
                    result += s[colIdx+i]

                nextCol = nextCol + 1

        return result


# 다른 사람의 풀이
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        lst = [""] * numRows
        i = 0
        up = 1 #bool

        for c in s:
            lst[i] += c

            if i == 0:
                up = 1
            elif i == numRows-1:
                up = 0

            if up:
                i += 1
            else:
                i -= 1
        
        return ''.join(lst)
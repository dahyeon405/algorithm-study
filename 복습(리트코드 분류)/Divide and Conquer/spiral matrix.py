import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        total = m*n

        loop = 0
        result = []
        i = 0
        k = 0

        while (loop < m/2 and loop < n/2):
            while i < m - loop and k < n - loop and i >= loop and k >= loop:
                if matrix[i][k] == -1000: break
                result.append(matrix[i][k])
                matrix[i][k] = -1000
                if i == loop:
                    if k == n - loop - 1:
                        i += 1
                    else: k += 1
                elif k == n - loop - 1:
                    if i == m - loop - 1:
                        k -= 1
                    else: i += 1
                elif i == m - loop - 1:
                    if k == loop:
                        i -= 1
                    else: k -= 1
                else:
                    if i == loop + 1: break
                    else: i -= 1
                
            loop += 1
            i = loop
            k = loop

        return result

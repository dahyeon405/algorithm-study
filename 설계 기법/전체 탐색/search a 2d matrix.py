class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for k in range(m):
                if matrix[i][k] == target: return True
                if matrix[i][k] > target: break

        return False
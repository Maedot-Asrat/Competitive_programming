# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for m in range(n):
            i = 0
            j= n-1
            while i < j:
                matrix[m][i], matrix[m][j] = matrix[m][j], matrix[m][i]
                i += 1
                j -= 1
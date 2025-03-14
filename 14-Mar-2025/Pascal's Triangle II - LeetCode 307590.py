# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1, rowIndex+1):
            temp = [1]*(i+1)
            temp[1] = i
            temp[-2] = i
            for j in range(2, i-1):
                temp[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(temp)
        return ans[rowIndex]
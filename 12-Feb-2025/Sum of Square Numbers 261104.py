# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=floor(math.sqrt(c))
        
        while left<=right:
            sum_square=left**2 + right**2
            if sum_square==c:
                return True
            if sum_square<c:
                left+=1
            else:
                right-=1
        return False
            
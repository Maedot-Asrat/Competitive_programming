# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        factor=self.fact(n)
        count=0
        while factor%10==0:
            count+=1
            factor=factor//10
        return count
    def fact(self,n):
        if n==0 or n==1:
            return 1
        return n * self.fact(n-1) 

    

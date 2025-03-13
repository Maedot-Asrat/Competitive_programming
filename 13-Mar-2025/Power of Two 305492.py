# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n%2!=0 or n==0:
            return False
        return self.powtwo(n)
    def powtwo(self,n):
        if n==2 or n==0:
            return True
        if n%2!=0:
            return False
        return self.powtwo(n//2)
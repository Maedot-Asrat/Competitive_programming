# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            n=-n
            x=1/x
        return self.mypower(x,n)
    def mypower(self,x,n):
        if n==1 or n==0:
            return x
        if n%2==0:
            half=self.mypower(x,n//2)
            return half* half
        else:
            return self.mypower(x,n-1) * x
        
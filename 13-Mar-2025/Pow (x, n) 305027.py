# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powe(x, n):
            if n == 0:
                return 1
            half = powe(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1 / x
            n = -n
        return powe(x, n)
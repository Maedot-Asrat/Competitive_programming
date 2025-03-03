# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros=s.count("0")
        ones=s.count("1")
        new_s="1" * (ones-1) + "0"*zeros + "1"
        return new_s
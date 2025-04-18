# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        count=0
        for element in s:
            if element=="R":
                r+=1
                if r==l:
                    count+=1
                    r=0
                    l=0
            elif element=="L":
                l+=1
                if r==l:
                    count+=1
                    r=0
                    l=0
        return count

# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        start=0
        end=len(s)-1
        swap=0
        while start<end:
            if s[start]=='1' and s[end]=='0':
                swap+=end-start
                end-=1
                start+=1
            elif s[end]=='0' and s[start]=='0':
                start+=1
            elif s[start]=='0' and s[end]=='1':
                start+=1
                end-=1
            else:
                end-=1
        return swap
            

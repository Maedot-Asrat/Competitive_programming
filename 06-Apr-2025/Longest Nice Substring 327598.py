# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        n=len(s)
        def nice(sub:str)->str:
            char=set(sub)
            for stringg in sub :
                if stringg.swapcase() not in char:
                    return False
            return True
        for i in range(n):
            for j in range(i+1,n+1):
                sub=s[i:j]
                if nice(sub) and len(sub)>len(ans):
                    ans=sub
        return ans
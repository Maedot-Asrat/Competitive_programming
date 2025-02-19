# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        maxi=0
        track={1:s.count('1')}
        new_s=''
        for i in range(len(s)-1):
            new_s+=s[i]
            summ=new_s.count('0') + track[1]-new_s.count('1')
            maxi=max(maxi,summ)
        return maxi
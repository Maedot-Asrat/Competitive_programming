# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_track=Counter(s1)
        window=len(s1)
        left=0
        while window<=len(s2):
            s2_track=Counter(s2[left:window])
            if s1_track == s2_track:
                return True
            left+=1
            window+=1
        return False
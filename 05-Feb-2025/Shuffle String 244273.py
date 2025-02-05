# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list=[0]*len(s)
        track=dict()
        for i in range(len(s)):
            track[i]=track.get(i,indices[i])
        for key,value in track.items():
            new_list[value]=s[key]
        return "".join(new_list)
        

      
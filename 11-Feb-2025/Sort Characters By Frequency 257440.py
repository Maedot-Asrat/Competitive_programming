# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        track=Counter(s)
        new_list=set(Counter(s).values())
        new_list=sorted(new_list,reverse=True)
        s=''
        for i in new_list:
            for key,value in track.items():
                if i==value:
                    s+=key*value
        return s
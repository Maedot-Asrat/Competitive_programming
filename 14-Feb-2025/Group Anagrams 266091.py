# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_string=[sorted(item) for item in strs]
        track=defaultdict(list)
        for i in range(len(strs)): 
            track[str(new_string[i])].append(strs[i])
        return list(track.values())
        



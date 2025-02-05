# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        track={}
        common=[]
        min_index_sum=float('inf')
        for item in list1:
            if item in list2:
                track[list1.index(item)]=track.get(list1.index(item), list2.index(item))
        for key,value in track.items():
            min_index_sum=min(min_index_sum, key+track[key])
        for key, value in track.items():
            if key+track[key]==min_index_sum:
                common.append(list1[key])
        return common

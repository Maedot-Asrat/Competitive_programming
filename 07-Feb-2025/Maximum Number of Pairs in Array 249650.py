# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        track=Counter(nums)
        pairs=0
        left_over=0
        for value in track.values():
            pairs+=value//2
            left_over+=value%2
        return [pairs,left_over]
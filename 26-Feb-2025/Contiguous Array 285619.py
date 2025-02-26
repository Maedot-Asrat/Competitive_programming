# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length=0
        track = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in track:
                max_length = max(max_length, index - track[count])
            else:
                track[count] = index
        
        return max_length
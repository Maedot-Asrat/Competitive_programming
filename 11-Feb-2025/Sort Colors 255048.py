# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        m=len(nums)
        for j in range(m):
            for i in range(m-1):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        
        
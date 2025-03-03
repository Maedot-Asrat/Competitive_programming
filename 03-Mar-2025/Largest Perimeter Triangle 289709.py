# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums , reverse=True)
        left=0
        right=2
        while right<len(nums):
            if nums[left+1]+nums[right]>nums[left]:
                return (nums[left]+nums[left+1]+nums[left+2])
            else:
                left+=1
                right+=1
        return 0



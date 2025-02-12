# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0)==len(nums):
            return "0"
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if str(nums[j])+str(nums[j+1])<str(nums[j+1])+str(nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        return "".join(nums)
        
        


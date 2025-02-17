# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev_sum=0
        i=0
        while i<len(nums):
            prev_sum+=nums[i]
            nums[i]=prev_sum
            i+=1
        return nums
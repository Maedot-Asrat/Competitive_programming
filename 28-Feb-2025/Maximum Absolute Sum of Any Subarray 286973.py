# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_res = nums[0]
        min_res = nums[0]
        maxEnding = nums[0]
        minEnding=nums[0]
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            max_res = max(max_res, maxEnding)
        for j in range(1, len(nums)):
            minEnding = min(minEnding + nums[j], nums[j])
            min_res = min(min_res, minEnding)
        return max(abs(max_res),abs(min_res))

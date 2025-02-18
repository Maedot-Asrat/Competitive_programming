# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum= float('-inf')
        curr_sum=0
        for i in nums:
            curr_sum+=i
            if curr_sum>maximum:
                maximum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return maximum

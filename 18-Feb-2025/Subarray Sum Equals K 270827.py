# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c_map = {0: 1} 
        prev_sum = 0
        count = 0
        for num in nums:
            prev_sum += num  
            if prev_sum - k in c_map:
                count += c_map[prev_sum - k]
            c_map[prev_sum] = c_map.get(prev_sum, 0) + 1
        return count
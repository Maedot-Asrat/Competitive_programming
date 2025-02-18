# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c_map = {0: 1} 
        prev_sum = 0
        count = 0
        for num in nums:
            prev_sum += num  
            if prev_sum - goal in c_map:
                count += c_map[prev_sum - goal]
            c_map[prev_sum] = c_map.get(prev_sum, 0) + 1
        return count
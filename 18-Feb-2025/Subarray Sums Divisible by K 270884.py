# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c_map = {0: 1} 
        prev_sum = 0
        count = 0
        for num in nums:
            prev_sum += num  
            if prev_sum%k in c_map:
                count += c_map[prev_sum%k]
            c_map[prev_sum%k] = c_map.get(prev_sum%k, 0) + 1
        return count
# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        track = {0:-1}
        rem = 0
        for i in range(len(nums)):
            rem += nums[i]
            rem %=k
            if rem not in track:
                track[rem] = i
            elif i - track[rem] >=2:
                return True
        return False
        
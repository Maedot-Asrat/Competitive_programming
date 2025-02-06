# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i],nums[i+1]= nums[i]*2 , 0
        count=0
        while 0 in nums:
            nums.remove(0)
            count+=1
        for _ in range(count):
            nums.append(0)
        return nums

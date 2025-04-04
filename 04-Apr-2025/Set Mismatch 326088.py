# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while i<len(nums):
            if nums[i]==nums[nums[i]-1]:
                i+=1
            else:
                temp=nums[i]
                nums[i] , nums[temp-1] = nums[temp-1], nums[i]
        j=0
        while j<len(nums):
            if nums[j]!=j+1:
                return [nums[j],j+1]
            j+=1
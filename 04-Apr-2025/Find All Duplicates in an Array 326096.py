# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while i<len(nums):
            if nums[i]==nums[nums[i]-1]:
                i+=1
            else:
                temp=nums[i]
                nums[i] , nums[temp-1] = nums[temp-1], nums[i]
        j=1
        while j<=len(nums):
            if nums[j-1]!=j:
                ans.append(nums[j-1])
            j+=1
        return ans
# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                ans.append(j)
            j+=1
        return ans



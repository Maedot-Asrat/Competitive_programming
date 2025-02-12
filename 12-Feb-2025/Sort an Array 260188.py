# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_nums=[0]*(max(nums)+1+abs(min(nums))) 
        minimum=abs(min(nums))
        for i in range(len(nums)):
            new_nums[nums[i]+minimum]+=1
        i=0
        j=0
        while i< len(new_nums):
            while new_nums[i]>0:
                nums[j]=i-minimum
                new_nums[i]-=1
                j+=1
            i+=1
        return nums
            


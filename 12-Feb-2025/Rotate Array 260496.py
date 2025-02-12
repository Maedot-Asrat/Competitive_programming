# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k==0 or len(nums)==1:
            nums=nums
        elif k>len(nums):
            k=k%len(nums)
            temp=nums[-k:]
            for j in range(len(nums)-1,k-1,-1):
                nums[j]=nums[j-k]
            nums[:k]=temp
        else:
            temp=nums[-k:]
            for j in range(len(nums)-1,k-1,-1):
                nums[j]=nums[j-k]
            nums[:k]=temp
                
        
        
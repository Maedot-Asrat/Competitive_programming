# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            target= -nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left-1]==nums[left] and left<right:
                        left+=1
                        
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        return list(set(tuple(triplet) for triplet in ans))
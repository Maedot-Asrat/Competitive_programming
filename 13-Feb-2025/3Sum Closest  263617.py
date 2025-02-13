# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        track=dict()
        if len(nums)==3:
            return sum(nums)
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                summ=nums[i]+nums[left]+nums[right]
                track[abs(target-summ)]=summ
                if summ<target:
                    left+=1
                elif summ>target:
                    right-=1
                else:
                    return summ
        close_target= min(track.keys())
        return track[close_target]

# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left=0
        if nums[0]==0 and len(nums)!=1:
            return False
        maxi=0
        while left<len(nums)-1:
            maxi=max(maxi, left+nums[left])
            if nums[left]>=len(nums)-left-1:
                return True
            if nums[left]==0 and left>=maxi:
                return False
            left+=1
        return True
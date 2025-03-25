# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        ans=[]
        def bs(nums, left, right):
            if left > right:
                return -1
            mid = (left + right)//2
            if target == nums[mid]:
                ans.append(mid)
                bs(nums, mid+1, right)
                bs(nums, left, mid-1)
            elif target < nums[mid]:
                return bs(nums, left, mid-1)
            else:
                return bs(nums, mid+1, right)
        bs(nums, left, right)
        if len(ans)>1:
            return [min(ans),max(ans)]
        elif len(ans)==1:
            ans.append(ans[0])
            return ans
        else:
            return [-1,-1]
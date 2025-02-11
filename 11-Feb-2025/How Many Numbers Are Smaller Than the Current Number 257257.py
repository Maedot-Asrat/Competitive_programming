# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        unsorted_nums=[x for x in nums]
        nums.sort()
        ans=[]
        for num in unsorted_nums:
            ans.append(nums.index(num))
        return ans
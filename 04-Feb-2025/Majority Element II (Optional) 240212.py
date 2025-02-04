# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        for key,value in Counter(nums).items():
            if value > floor(len(nums)/3):
                ans.append(key)
        return ans

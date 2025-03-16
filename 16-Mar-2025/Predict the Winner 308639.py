# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        arr = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            arr[i] = nums[i]
            for j in range(i+1, len(nums)):
                arr[j] = max(nums[i]-arr[j],nums[j]-arr[j-1])
        return arr[len(nums)-1] >= 0
# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky=[]
        for key, value in Counter(nums).items():
            if value==2:
                sneaky.append(key)
        return sneaky
# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_con=0
        while left<right:
            max_con=max(max_con, (min(height[left],height[right])*(right-left)))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_con
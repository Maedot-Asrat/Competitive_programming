# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix_prod = 1
        for i in range(n):
            ans[i] = prefix_prod
            prefix_prod *= nums[i]
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans


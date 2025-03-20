# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(temp):
            if len(temp)==len(nums):
                ans.append(temp[:])
                return 
            for num in nums :
                if num not in temp:
                    temp.append(num)
                    backtrack(temp)
                    temp.pop()
        ans=[]
        backtrack([])
        return ans
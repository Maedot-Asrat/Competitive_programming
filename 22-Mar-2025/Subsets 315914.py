# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(temp):
            if  temp not in ans:
                ans.append(temp[:])
            else:
                return
            for num in nums:
                if  num not in temp:
                    temp.append(num)
                    backtrack(sorted(temp))
                    temp.pop()
        temp=[]
        ans=[]
        backtrack(temp)
        return ans
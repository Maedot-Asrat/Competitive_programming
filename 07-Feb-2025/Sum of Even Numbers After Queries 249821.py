# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        sum=0
        for num in nums:
            if num%2==0:
                sum+=num
        for i in range(len(queries)):
            if nums[queries[i][1]]%2==0:
                sum-=nums[queries[i][1]]
            nums[queries[i][1]]=nums[queries[i][1]] + queries[i][0]
            if nums[queries[i][1]]%2==0:
                sum+=nums[queries[i][1]]
            ans.append(sum)
        return ans
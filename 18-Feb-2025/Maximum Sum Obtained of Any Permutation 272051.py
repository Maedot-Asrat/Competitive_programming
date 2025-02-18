# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        track=[0]*(len(nums)+1)
        nums.sort(reverse=True)
        max_sum=0
        for item in requests:
            track[item[0]]+=1
            track[item[1]+1]-=1
        i=1
        while i<len(track):
            track[i]+=track[i-1]
            i+=1
        track.sort(reverse=True)
        j=0

        print(track)
        while j < len(track) and track[j]!=0:
            max_sum+=track[j]*nums[j]
            j+=1
        return max_sum%(10**9 + 7)

            
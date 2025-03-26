# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(mid):
            count=0
            curr=0
            for i in weights:
                curr+=i
                if curr>mid:
                    count+=1
                    curr=i
            return count+1<=days
        low = max(weights)
        high = sum(weights)
        ans=float('inf')
        while low <= high:
            mid = (low+high)//2
            if is_valid(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
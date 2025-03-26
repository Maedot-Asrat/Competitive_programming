# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_valid(mid):
            summ=0
            for i in ranks:
                summ+= floor(math.sqrt(mid//i))
            if summ>=cars:
                return True
            else:
                return False
        low = min(ranks)
        high = min(ranks)*cars*cars
        ans=float('inf')
        while low <= high:
            mid = (low+high)//2
            if is_valid(mid):
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans
# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: 
            return 0
        n = len(citations)
        init, end = 0, n - 1
        while init <= end:
            mid = (init + end)//2
            if mid + citations[mid] >= n:
                end = mid - 1
            else:
                init = mid + 1                
        return n - init
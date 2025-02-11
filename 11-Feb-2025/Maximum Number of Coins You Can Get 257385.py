# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_pile=0
        count=0
        i=2
        n=len(piles)
        while i<n and count<n/3:
            max_pile+=piles[-i]
            count+=1
            i+=2
        return max_pile

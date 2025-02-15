# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=0
        right=len(cardPoints)-k
        total_sum=sum(cardPoints)
        maxi=total_sum - sum(cardPoints[left:right])
        window=sum(cardPoints[left:right])
        while right<len(cardPoints):
            window=window-cardPoints[left]+cardPoints[right]
            maxi=max(maxi,total_sum-(window))
            left+=1
            right+=1
        return maxi
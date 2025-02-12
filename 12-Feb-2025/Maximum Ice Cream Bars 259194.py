# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        icecream=[0]*(max(costs)+1)
        for cost in costs:
            icecream[cost]+=1
        count=0
        total_bar=0
        for i in range(len(icecream)):
            if total_bar<coins and icecream[i]!=0 :
                for _ in range(icecream[i]):
                    total_bar+= i
                    if total_bar<=coins:
                        count+=1
            elif icecream[i]==0:
                continue
            else:
                break
           
        return count
                

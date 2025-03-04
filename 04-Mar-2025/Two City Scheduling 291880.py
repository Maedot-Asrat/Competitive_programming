# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        i=0
        total=0
        while i<len(costs):
            if i <len(costs)/2:
                total+=costs[i][0]
            else:
                total+=costs[i][1]
            i+=1
        return total
# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people.sort()
        left=0
        right=len(people)-1
        if len(people)==2 and sum(people)<=limit:
            return 1
        while left<=right:
            if people[-1]>=limit:
                people.pop()
                count+=1
                right=len(people)-1
            elif people[left]+people[right]<=limit:
                count+=1
                left+=1
                right-=1
            else:
                count+=1
                right-=1
        return count
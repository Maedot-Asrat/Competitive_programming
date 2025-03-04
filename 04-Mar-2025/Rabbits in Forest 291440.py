# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for key,value in count.items():
            if key==value:
                total+=key+1
            elif value<key:
                total+=key+1
            else:
                total+= ceil(value/(key+1)) * (key+1)
        return total
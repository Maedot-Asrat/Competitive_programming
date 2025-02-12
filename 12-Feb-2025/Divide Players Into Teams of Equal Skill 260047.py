# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        skill_sum=[skill[left],skill[right]]
        ans=0
        while left<right:
            if sum(skill_sum)==sum([skill[left],skill[right]]):
                ans+=skill[left]*skill[right]
                left+=1
                right-=1
            else:
                return -1
        return ans

            

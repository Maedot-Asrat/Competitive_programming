# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billss=defaultdict(int)
        for bill in bills:
            billss[bill]+=1
            if bill==10:
                if 5 not in billss:
                    return False
                elif billss[5]>0:
                    billss[5]-=1
                else:
                    return False
            elif bill==20:
                if billss[10]>0 and billss[5]>0:
                    billss[10]-=1
                    billss[5]-=1
                elif billss[5]>=3:
                    billss[5]-=3
                else:
                    return False
            else:
                continue
        return True
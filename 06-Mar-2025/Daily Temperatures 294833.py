# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        track=defaultdict(int)
        mono_stack=[]
        for temp in range(len(temperatures)):
            while mono_stack and temperatures[mono_stack[-1]]<temperatures[temp]:
                top=mono_stack.pop()
                track[top] = temp
            mono_stack.append(temp)
        for i in range(len(temperatures)):
            if i not in track:
                temperatures[i]=0
            else:
                temperatures[i]=track[i]-i
        return temperatures
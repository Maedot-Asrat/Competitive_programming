# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        for elem in s:
            if elem!="#":
                stack_s.append(elem)
            else:
                if len(stack_s)>0:
                    stack_s.pop()
        for elem in t:
            if elem!="#":
                stack_t.append(elem)
            else:
                if len(stack_t)>0:
                    stack_t.pop()
        return stack_s==stack_t
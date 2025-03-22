# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token=='+':
                stack.append(stack.pop() + stack.pop())
                continue
            elif token== '*':
                stack.append(stack.pop() * stack.pop())
                continue
            elif token== '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                continue
            elif token== '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
                continue
            else:
                stack.append(int(token))
        return stack.pop()
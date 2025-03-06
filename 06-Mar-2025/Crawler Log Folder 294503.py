# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for log in logs:
            if len(log)>=3:
                if log[-3]==".":
                    if len(stack)>0:
                        stack.pop()
                elif log[-2]==".":
                    continue
                else:
                    stack.append(log)
            else:
                if log[-2]==".":
                    continue
                else:
                    stack.append(log)
        return len(stack)
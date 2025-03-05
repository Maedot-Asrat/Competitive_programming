# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path=list(path.split("/"))
        print(path)
        ans=[]
        if new_path[-1]=="":
            new_path.pop
        for i in range(len(new_path)):
            if new_path[i]==".":
                continue
            elif new_path[i]=="..":
                if len(ans)!=0:
                    ans.pop()
            elif new_path[i]=="":
                continue
            else:
                ans.append(new_path[i])
        ans="/".join(ans)
        ans= "/" + ans
        return ans
            
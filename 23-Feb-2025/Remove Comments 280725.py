# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        all_s = "\n".join(source)
        result= ""
        i = 0
        while i < len(all_s):
            two = all_s[i:i+2]
            if two == "//":
                i += 2
                while i < len(all_s) and all_s[i] != "\n":
                    i += 1
            elif two == "/*":
                i += 2
                while all_s[i:i+2] != "*/":
                    i += 1
                i += 2
            else:
                result += all_s[i]
                i += 1
        ans = []
        for line in result.split("\n"):
            if line != "":
                ans.append(line)
        return ans

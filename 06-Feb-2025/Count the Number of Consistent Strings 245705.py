# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent=0
        allowed_count=Counter(allowed)
        for word in words:
            for char in word:
                if char not in allowed:
                    consistent+=1
                    break
            # if Counter(word).keys() <= allowed_count.keys():
            #     consistent+=1
        return len(words)-consistent
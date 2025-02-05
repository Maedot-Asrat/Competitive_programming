# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        flag = True
        for word in words:
            flag = True
            for char in word:
                if chars.count(char) < word.count(char):
                    flag = False
                    break
            if flag is True:
                sum += len(word)
        return sum
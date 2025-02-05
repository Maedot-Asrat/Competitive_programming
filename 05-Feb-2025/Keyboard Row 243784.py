# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow="qwertyuiop"
        first_dict=Counter(firstrow)
        secondrow="asdfghjkl"
        second_dict=Counter(secondrow)
        thirdrow="zxcvbnm"
        third_dict=Counter(thirdrow)
        output=[]
        for word in words:
            if Counter(word.lower()).keys() <= first_dict.keys()  or Counter(word.lower()).keys() <= second_dict.keys() or Counter(word.lower()).keys() <= third_dict.keys():
                output.append(word)
        return output
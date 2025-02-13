# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                if s[left]==s[right-1] or s[left+1]==s[right]:
                    new_arr=s[left:right]
                    new_ar=s[left+1:right+1]
                    return new_arr==new_arr[::-1] or new_ar==new_ar[::-1]
                else:
                    return False
            left+=1
            right-=1
        return True

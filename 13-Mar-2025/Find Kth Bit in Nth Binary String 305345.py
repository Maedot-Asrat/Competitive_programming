# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans=self.findkth(n,k)
        return ans[k-1]
    def findkth(self,n,k):
        if n==1:
            return "0"
        return self.findkth(n-1,k) +"1"+ self.invert(self.findkth(n-1,k))[::-1]
    def invert(self,s):
        new_s=[]
        for i in s:
            if i=='0':
                new_s.append('1')
            else:
                new_s.append('0')
        return "".join(new_s)
    



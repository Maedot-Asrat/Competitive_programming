# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums=[]

    def add(self, num: int) -> None:
        if num==0:
            self.nums=[]
        else:
            if len(self.nums)==0:
                self.nums.append(num)
            else:
                self.nums.append(num*self.nums[-1])
    def getProduct(self, k: int) -> int:
        if k>len(self.nums):
            return 0
        if k==len(self.nums):
            return self.nums[-1]
        else:
            return int(self.nums[-1]/self.nums[-k-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
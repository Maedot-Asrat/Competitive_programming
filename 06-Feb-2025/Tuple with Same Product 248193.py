# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]*nums[j] not in dic:
                    dic[nums[i]*nums[j]] = []
                dic[nums[i]*nums[j]].append((nums[i], nums[j]))
        res = 0
        for i in dic:
            if len(dic[i]) >1:
                res+=len(dic[i])*(len(dic[i])-1)*4
        return res
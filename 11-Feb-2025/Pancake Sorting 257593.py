# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

import random
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        sorted_arr=sorted(arr)
        for i in range(len(arr),0,-1):
            max_num = max(arr[:i])
            k= arr.index(max_num) + 1
            arr=arr[:k][::-1]+arr[k:]
            ans.append(k)
            arr=arr[:i][::-1] + arr[i:]
            ans.append(i)
            if arr== sorted_arr:
                break
        return ans

        

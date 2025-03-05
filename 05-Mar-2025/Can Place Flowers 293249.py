# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        i=0
        if len(flowerbed)==1:
            if n>1:
                return False
            else:
                if flowerbed[0]==0:
                    return True
                elif n==0:
                    return True
                else:
                    return False
        while i<len(flowerbed):
            if i==0 and flowerbed[0]==0 and flowerbed[1]==0:
                count+=1
                i+=2
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                count+=1
                i+=2
            elif flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                count+=1
                i+=2
            else:
                i+=1
        if count>=n:
            return True
        else:
            return False
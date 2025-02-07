# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            new_mat=[list(x)[::-1] for x in zip(*mat)]
            if new_mat==target:
                return True
            mat=new_mat
        return False
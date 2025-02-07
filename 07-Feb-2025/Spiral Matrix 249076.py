# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new_list=[]
        while len(matrix)!=0:
            new_list.extend(matrix.pop(0))
            print(new_list)
            for i in range(0,len(matrix)):
                if len(matrix[i])!=0:
                    new_list.append(matrix[i].pop(-1))
            
            if len(matrix)!=0:
                lii=matrix.pop(len(matrix)-1)
                new_list.extend(lii[::-1])
            for j in range(len(matrix)-1,0,-1):
                if len(matrix[j])!=0:
                    new_list.append(matrix[j].pop(0))
        
        return new_list
          
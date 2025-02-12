# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        track=dict()
        ans=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in track:
                    track[i+j]=[]
                track[i+j].append([i,j])
        for key,value in track.items():
            if key%2==0:
                value=value[::-1]
                for item in value:
                    ans.append(mat[item[0]][item[1]])
            else:
                for item in value:
                    ans.append(mat[item[0]][item[1]])
            
        return ans
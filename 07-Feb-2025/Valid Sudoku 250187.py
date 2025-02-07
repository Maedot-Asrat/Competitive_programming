# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        new_board=[list(x) for x in zip(*board)]
        for i in range(9):
            count_i=Counter(board[i])
            for key in count_i:
                if key.isalnum() and count_i[key]!=1:
                    return False
            count_j=Counter(new_board[i])
            for key in count_j:
                if key.isalnum() and count_j[key]!=1:
                    return False
        i=0
        
        new_list=[]
        while i<9:
            j=0
            while j<9:
                if board[i][j].isalnum():
                    new_list.append(board[i][j])
                if board[i+1][j].isalnum():
                    new_list.append(board[i+1][j])
                if board[i+2][j].isalnum():
                    new_list.append(board[i+2][j])
                if j==2 or j==5 or j==8:
                    print(new_list)
                    print(set(new_list))
                    if sorted(new_list)!=list(sorted(set(new_list))):
                        return False
                    new_list=[]
                j+=1
            i+=3
        return True
# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

class solution:
    def bomb_validation():
        n,m=input().split()
        matrix=[[0]*int(m) for _ in range(int(n))]
        for i in range(int(n)):
            accept=list(input())
            matrix[i]=accept
        flag="YES"
        for i in range(int(n)):
             for j in range(int(m)):
                count=0
                if i<int(n)-1 and matrix[i+1][j]=="*":
                    count+=1
                if j<int(m)-1 and matrix[i][j+1]=="*":
                    count+=1
                if i<int(n)-1 and j<int(m)-1 and matrix[i+1][j+1]=="*":
                    count+=1
                if i!=0 and matrix[i-1][j]=="*":
                    count+=1
                if j!=0 and matrix[i][j-1]=="*":
                    count+=1
                if i!=0 and j!=0 and matrix[i-1][j-1]=="*":
                    count+=1
                if i!=0 and j<int(m)-1 and matrix[i-1][j+1]=="*":
                    count+=1
                if i<int(n)-1 and j!=0 and matrix[i+1][j-1]=="*":
                    count+=1
                if matrix[i][j]=="." and count!=0:
                    flag="NO"
                if matrix[i][j]!="*" and matrix[i][j]!="." and int(matrix[i][j])!=count:
                    flag="NO"
        print(flag)
    bomb_validation()
# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def x_Sum(ques, row, col):
    maxx = 0
    for i in range(row):
        for j in range(col):
            adds = ques[i][j]
            k = i
            z = j
            adds+=tleft(ques,k, z, row, col)
            k = i
            z = j
            adds+=tright(ques, k, z, row, col)
            k = i
            z = j
            adds+=bleft(ques, k, z, row, col)
            k = i
            z = j
            adds+=bright(ques, k, z, row, col)
            maxx = max(maxx, adds)
    return maxx
def tleft(ques, n, m, row, col):
    summ = 0
    n-=1
    m-=1
    while n >= 0 and m >= 0:
        summ+=ques[n][m]
        n-=1
        m-=1
    return summ
def tright(ques, n, m, row, col):
    summ = 0
    n-=1
    m+=1
    while n >= 0 and m < col:
        summ+=ques[n][m]
        n-=1
        m+=1
    return summ
def bleft(ques, n, m, row, col):
    summ = 0
    n+=1
    m-=1
    while n < row and m >= 0:
        summ+=ques[n][m]
        n+=1
        m-=1
    return summ
def bright(ques, n, m, row, col):
    summ = 0
    n+=1
    m+=1
    while n < row and m < col:
        summ+=ques[n][m]
        n+=1
        m+=1
    return summ

n = int(input())
for i in range(n):
    array = list(map(int, input().split()))
    ques = []
    for i in range(array[0]):
        arr = list(map(int, input().split()))
        ques.append(arr)
    print(x_Sum(ques, array[0], array[1]))

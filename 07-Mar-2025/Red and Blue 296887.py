# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    r=int(input())
    red=list(map(int, input().split()))
    b=int(input())
    blue=list(map(int, input().split()))
    for i in range(1,r):
        red[i]+=red[i-1]
    for j in range(1,b):
        blue[j]+=blue[j-1]
    maxi=0
    redd=max(red)
    blued=max(blue)
    if redd>0:
        maxi+=redd
    if blued>0:
        maxi+=blued
    print(maxi)
# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    count=0
    i=0
    while i<n-1:
        if arr[i]>arr[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    print(count)
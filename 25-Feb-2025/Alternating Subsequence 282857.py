# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    sum = 0
    total= 0
    while i < n:
        while i < n and arr[i] < 0:
            sum = arr[i] if sum == 0 else max(sum, arr[i])
            i += 1
        total += sum
        sum = 0
        while i < n and arr[i] > 0:
            sum = max(sum, arr[i])
            i += 1
        total += sum
        sum = 0
    print(total)
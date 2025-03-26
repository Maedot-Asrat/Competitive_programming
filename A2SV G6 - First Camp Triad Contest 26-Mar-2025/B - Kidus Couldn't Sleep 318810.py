# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n, k = map(int, input().split()) 
a = list(map(int, input().split()))
curr = sum(a[:k])
total = curr
for i in range(k, n):
    curr += a[i] - a[i - k]
    total += curr

print(total / (n - k + 1))
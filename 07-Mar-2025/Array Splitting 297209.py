# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))
differences = [arr[i] - arr[i - 1] for i in range(1, n)]
differences.sort(reverse=True)
largest_gaps = sum(differences[:k - 1])
total_cost = arr[-1] - arr[0] - largest_gaps
print(total_cost)

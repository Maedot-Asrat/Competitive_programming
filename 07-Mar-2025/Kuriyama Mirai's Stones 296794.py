# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

t=int(input())
costs= list(map(int, input().split()))
arranged_costs=sorted(costs)
n=int(input())
for i in range(1,t):
    costs[i]+=costs[i-1]
for i in range(1,t):
    arranged_costs[i]+=arranged_costs[i-1]
for _ in range(n):
    type, l, r =map(int, input().split())
    if type==1:
        if l!=1:
            print(costs[r-1]-costs[l-2])
        else:
            print(costs[r-1])
    else:
        if l!=1:
            print(arranged_costs[r-1]-arranged_costs[l-2])
        else:
             print(arranged_costs[r-1])

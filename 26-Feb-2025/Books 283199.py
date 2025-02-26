# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=(map(int, input().split()))
arr=list(map(int, input().split()))
start=0
end=0
summ=0
ans=0
while end<len(arr) and start<len(arr):
    summ+=arr[end]
    if summ<=t:
        ans=max(ans,end-start+1)
    else:
        summ-=arr[start]
        start+=1
    end+=1
print(ans)
        
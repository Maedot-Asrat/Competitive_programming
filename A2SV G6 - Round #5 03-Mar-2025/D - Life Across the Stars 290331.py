# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict, Counter
t= int(input())
track=defaultdict(int)
for _ in range(t):
    b,d=map(int, input().split())
    track[b]+=1
    track[d]-=1
track=dict(sorted(track.items()))
years=list(track.keys())
pref_sum=[0]+ list(track.values())
for i in range(1,len(pref_sum)):
    pref_sum[i]+=pref_sum[i-1]
maxi=max(pref_sum)
year=0
for j in range(len(track)):
    if pref_sum[j]==maxi:
        year=years[j-1]
        break
print(year, maxi)



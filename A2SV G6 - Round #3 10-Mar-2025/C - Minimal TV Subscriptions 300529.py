# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
def check(shows,n,d):
    left=0
    right=d
    track=Counter(shows[left:right])
    window=len(track)
    if len(shows)==d:
        return window
    while right<n:
        if shows[right]!= shows[left]:
            track[shows[left]] -= 1
        if track[shows[left]] == 0:
            del track[shows[left]]
        if shows[right]!=shows[left]:
            track[shows[right]] += 1
        window = min(window, len(track))
        left += 1
        right += 1
    
    return window
t=int(input())
for _ in range(t):
    n,k,d=map(int, input().split())
    shows=list(map(int,input().split()))
    print(check(shows,n,d))

# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track=dict()
        for num in nums:
            track[num]=track.get(num,0) + 1
        print(track)
        freq= list(track.values())
        freq.sort()
        ans=[]
        freq=freq[::-1]
        wanted=freq[0:k]
        for key,value in track.items():
            if value in wanted and len(ans)!=k:
                ans.append(key)
        return ans

        
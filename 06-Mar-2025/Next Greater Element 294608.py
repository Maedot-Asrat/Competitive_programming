# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track=defaultdict(int)
        ans=[]
        for i in range(len(nums2)):
            for j in range(i,len(nums2)):
                if nums2[i]<nums2[j]:
                    track[nums2[i]]=nums2[j]
                    break
            if nums2[i] not in track:
                track[nums2[i]]=-1
        for num in nums1:
            ans.append(track[num])
        return ans
            
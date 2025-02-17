# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        track=Counter(word)
        track_values=list(track.values())
        tracker=set(track.values())
        if len(tracker)==2:
            if track_values.count(min(tracker))==1 and min(tracker)==1:
                return True
            elif track_values.count(max(tracker))==1:
                return abs(max(tracker) - min(tracker))==1
            else:
                return False
        elif max(tracker)==1:
            return True
        elif len(tracker)==1 and len(track_values)==1:
            return True
        else:
            return False

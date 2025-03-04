# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves=0
        if maxDoubles==0:
            moves+=target-1
            return moves
        while maxDoubles>0 and target>1:
            if target%2==0:
                moves+=1
                target=target/2
            else:
                moves+=2
                target=target//2
            maxDoubles-=1
        return int(moves+target-1)

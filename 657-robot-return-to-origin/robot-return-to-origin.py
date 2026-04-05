class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,d =moves.count('U'),moves.count('D')
        r,l = moves.count('R'), moves.count('L')
        return u == d and r == l
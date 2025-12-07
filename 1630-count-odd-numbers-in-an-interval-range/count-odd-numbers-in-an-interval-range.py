class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ceil((high - low +1)/2) if low%2 == 1 and high%2 == 1 else (high-low+1)//2
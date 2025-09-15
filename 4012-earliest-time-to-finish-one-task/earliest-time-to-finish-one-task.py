class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mn=10**60
        for i in tasks:
            mn=min(mn, i[0] + i[1])
        return mn
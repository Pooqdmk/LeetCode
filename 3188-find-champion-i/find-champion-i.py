class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        mx=-1
        curr=-1
        for i in range(len(grid)):
            prev=mx
            mx=max(mx,grid[i].count(1))
            if prev!=mx:
                curr=i
            
        return curr

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid) 
        seen=set([i for i in range(1,n**2+1)])
        elem=0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    seen.remove(grid[i][j])
                else:
                    elem=grid[i][j]
                    
        return [elem]+list(seen)
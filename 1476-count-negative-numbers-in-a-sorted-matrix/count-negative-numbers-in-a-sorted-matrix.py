class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        cnt=0
        for i in range(n):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j]<0:
                    cnt+=1
                else:
                    break
        return cnt
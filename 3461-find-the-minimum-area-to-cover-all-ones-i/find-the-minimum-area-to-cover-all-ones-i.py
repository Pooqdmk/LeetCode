class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        mn_row,mx_row,mn_col,mx_col=n,-1,m,-1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mn_row=min(mn_row,i)
                    mx_row=max(mx_row,i)
                    mn_col=min(mn_col,j)
                    mx_col=max(mx_col,j)
        return (mx_row-mn_row+1)*(mx_col-mn_col+1)
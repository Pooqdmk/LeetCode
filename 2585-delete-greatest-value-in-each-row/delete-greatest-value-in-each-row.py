class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        cnt=0
        # n=len(grid)
        while len(grid[0])>=1:
            mx=-1
            for i in range(len(grid)):
                elem=max(grid[i])
                index=grid[i].index(elem)
                grid[i]=grid[i][:index]+grid[i][index+1:]
                mx=max(mx,elem)
            cnt+=mx
        # cnt+=mx
        return cnt

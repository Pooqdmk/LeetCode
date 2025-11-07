class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid),len(grid[0])
        visited = set()
        res = 0

        def bfs(i,j):
            q = deque()
            visited.add((i,j))
            q.append((i,j))
            while q:
                i,j = q.popleft()
                d = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in d:
                    row,col = i+dr,j+dc
                    if row in range(r) and col in range(c) and grid[row][col] == '1' and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    res+=1
        return res


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]

        for r,c in guards:
            grid[r][c] = 'g'
        for r,c in walls:
            grid[r][c] = 'w'
        
        def is_guarded(r,c):
            for row in range(r+1,m):
                if grid[row][c] in ['g','w']:
                    break
                grid[row][c] = 'c'
            
            for row in reversed(range(0,r)):
                if grid[row][c] in ['g','w']:
                    break
                grid[row][c] = 'c'
            
            for col in range(c+1,n):
                if grid[r][col] in ['g','w']:
                    break
                grid[r][col] = 'c'
            
            for col in reversed(range(0,c)):
                if grid[r][col] in ['g','w']:
                    break
                grid[r][col] = 'c'
            

        for r,c in guards:
            is_guarded(r,c)
        
        return sum(r.count(0) for r in grid)
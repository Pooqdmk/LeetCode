class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n,m = len(board), len(board[0])
        w = len(word)
        if n == 1 and m == 1 and w == 1:
            return board[0][0] == word
        def dfs(i,j,idx):
            if idx == w:
                return True
            
            if board[i][j] != word[idx]:
                return False
            ch = board[i][j]
            board[i][j] = '*'

            for l,k in [(0,1),(1,0),(-1,0),(0,-1)]:
                r,c = i+l,j+k
                if 0 <= r < n and 0 <= c < m:
                    if dfs(r,c,idx+1):
                        return True
            board[i][j] = ch
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False


            

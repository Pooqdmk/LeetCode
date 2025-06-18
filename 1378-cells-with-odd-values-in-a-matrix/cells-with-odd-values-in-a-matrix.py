class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat=[[0]*n for _ in range(m)]
        
        for row,col in indices:
            for i in range(n):
                mat[row][i]+=1
            for j in range(m):
                mat[j][col]+=1
            

        cnt=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2!=0:
                    cnt+=1
        return cnt
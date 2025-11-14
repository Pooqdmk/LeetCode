class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        mat = [[0]*n for _ in range(n)]

        ad = [[0]*(n+1) for _ in range(n+1)]

        for r1,c1,r2,c2 in queries:
            ad[r1][c1]+=1
            ad[r2+1][c1]-=1
            ad[r1][c2+1]-=1
            ad[r2+1][c2+1]+=1
        
        for i in range(n):
            for j in range(n):
                mat[i][j] = ad[i][j]
                if i-1 > -1:
                    mat[i][j]+=mat[i-1][j]
                if j-1 > -1:
                    mat[i][j]+=mat[i][j-1]
                if i-1 > -1 and j-1 > -1:
                    mat[i][j]-=mat[i-1][j-1]
        return mat

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = [[0 for _ in range(c)]for _ in range(r)]
        n,m = len(mat), len(mat[0])
        if r*c > n*m or r*c < n*m:
            return mat
        p,k = 0,0
        for i in range(r):
            for j in range(c):
                l[i][j] = mat[k][p]
                if p+1 < m:
                    p+=1
                elif k+1 < n:
                    k+=1
                    p = 0
        return l
        
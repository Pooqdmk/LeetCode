class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):

            if mat == target:
                return True
            
            n,m = len(mat),len(mat[0])
            b = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    b[j][n-i-1] = mat[i][j]
            mat = b

        return False

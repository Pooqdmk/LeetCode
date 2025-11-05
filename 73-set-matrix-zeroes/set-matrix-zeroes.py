class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n,m =len(matrix),len(matrix[0])
        z = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    z.append([i,j])
                
        for r,c in z:
            
            for i in range(m):
                matrix[r][i] = 0
            for j in range(n):
                matrix[j][c] = 0
        
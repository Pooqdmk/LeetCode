class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        mat = [[0] * cols for _ in range(rows)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mat[i][j]=matrix[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=mat[j][i]
        for i in matrix:
            i.reverse()
            
        return matrix
        
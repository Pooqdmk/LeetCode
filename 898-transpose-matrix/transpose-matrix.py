class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols=len(matrix),len(matrix[0])
        mat=[rows*[0] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                mat[j][i]=matrix[i][j]
        return mat
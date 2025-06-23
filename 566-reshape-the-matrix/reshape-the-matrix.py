class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat

        matrix=[[0]*c for _ in range(r)]

        mat_1d=sum(mat,[])
        k=0
        for i in range(r):
            for j in range(c):
                matrix[i][j]=mat_1d[k]
                k+=1

        return matrix

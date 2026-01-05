class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt = 0
        s = 0
        mn = 10**6 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    cnt+=1
                    
                s+=abs(matrix[i][j])
                mn = min(mn, abs(matrix[i][j]))
                
        if cnt%2 == 0:
            return s
        return s-2*mn
class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        d=defaultdict(list)
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                d[i-j].append(mat[i][j])
        
        l=d.values()
        for i in l:
            if len(set(i)) != 1:
                return False
        return True
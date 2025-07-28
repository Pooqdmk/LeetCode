class Solution:
    def checkValid(self, mat: List[List[int]]) -> bool:
        n=len(mat)
        s=set([i for i in range(1,n+1)])
        for i in range(n):
            if set(mat[i]) != s:
                return False

        for j in range(n):
            seen=set()
            for i in range(n):
                if mat[i][j] not in seen:
                    seen.add(mat[i][j])
            if seen != s:
                return False

        return True
                
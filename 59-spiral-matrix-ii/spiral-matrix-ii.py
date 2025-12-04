class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for j in range(n)] for i in range(n)]
        l,r,t,b = 0,n,0,n
        num = 1
        while l<r and t<b:
            for i in range(l,r):
                mat[t][i] = num
                num+=1
            t+=1

            for i in range(t,b):
                mat[i][r-1] = num
                num+=1
            r-=1

            if not(l<r and t<b):
                break
            for i in range(r-1,l-1,-1):
                mat[b-1][i] = num
                num+=1
            b-=1
            for i in range(b-1,t-1,-1):
                mat[i][l] = num
                num+=1
            l+=1
        return mat

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        up=True
        r,c=0,0
        res=[]
        while r<n and c<m:
            if up:

                while c<m-1 and r>0:
                    res.append(mat[r][c])
                    r-=1
                    c+=1
                res.append(mat[r][c])
                if c==(m-1):
                    r+=1
                else:

                    c+=1
                
            else:

                while c>0 and r<n-1:
                    res.append(mat[r][c])
                    c-=1
                    r+=1
                res.append(mat[r][c])
                if r==n-1:
                    c+=1
                else:
                    r+=1
                
            up= not up

        return res



class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        n,m = rows, len(encodedText)//rows
        mat = [[0]*m for i in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                mat[i][j] = encodedText[k]
                k+=1
        i,j = 0,0
        r = 0
        res = []
        while i < n and j < m:
            res.append(mat[i][j])
            i+=1
            j+=1
            if i == n:
                r+=1
                i = 0
                j=r
        return ''.join(res).rstrip()
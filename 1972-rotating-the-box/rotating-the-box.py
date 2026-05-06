class Solution:
    def rotateTheBox(self, b: List[List[str]]) -> List[List[str]]:
        n,m = len(b), len(b[0])
        t = []
        for i in range(n):
            e,s = 0,0
            temp = []
            for j in range(m):
                if b[i][j] == '*':
                    temp.extend(['.']*e)
                    temp.extend(['#']*s)
                    temp.extend('*')
                    e,s =0,0
                elif b[i][j] == '#':
                    s+=1
                else:
                    e+=1
            if e>0 or s>0:
                temp.extend(['.']*e)
                temp.extend(['#']*s)
            t.append(temp)
        res = [['.' for j in range(n)]for i in range(m)]
        print(res)
        r,c = 0,-1
        for i in range(n):
            for j in range(m):
                res[r][c] = t[i][j]
                r+=1
                if r >= m:
                    c-=1
                    r=0
        return res

                

        
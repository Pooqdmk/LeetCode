class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        l = [n+1]*(n+1)
        r = [0]*(n+1)

        t = [0]*(n+1)
        b = [n+1]*(n+1)

        for i,j in buildings:
            l[j] = min(l[j],i)
            r[j] = max(r[j],i)

            t[i] = max(t[i],j)
            b[i] = min(b[i],j)
        cnt = 0
        for i,j in buildings:
            if i> l[j] and i<r[j] and j>b[i] and j<t[i]:
                cnt+=1
        return cnt

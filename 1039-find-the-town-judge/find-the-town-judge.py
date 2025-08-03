class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return n if n==1 else -1
        
        t=[0]*(n+1)

        for (a,b) in trust:
            t[a]-=1
            t[b]+=1

        for i in range(1,n+1):
            if t[i] == n-1:
                return i
        return -1
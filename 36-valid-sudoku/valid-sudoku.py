class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        n=len(b)
        m=len(b[0])
        
        for i in range(n):
            s=set()
            for j in range(m):
                if b[i][j]!='.':
                    if b[i][j] not in s:
                        s.add(b[i][j])
                    else:
                        return False        
        for j in range(m):
            s=set()
            for i in range(n):
                if b[i][j] != '.':
                    if b[i][j] not in s:
                        s.add(b[i][j])
                    else:
                        return False
        
        d=defaultdict(set)

        for i in range(n):
            for j in range(m):
                if b[i][j]!='.':
                    a=i//3 
                    c=j//3
                    if b[i][j] not in d[(a,c)]:
                        d[(a,c)].add(b[i][j])
                    else:
                        return False
        return True


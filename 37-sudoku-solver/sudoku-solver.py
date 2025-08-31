class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        row=defaultdict(set)
        col=defaultdict(set)
        sq=defaultdict(set)
        emp=[]
        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    emp.append((i,j))
                else:
                    row[i].add(b[i][j])
                    col[j].add(b[i][j])
                    sq[(i//3)*3+j//3].add(b[i][j])

        def backtrack(k=0):

            if k == len(emp):
                return True
            
            i,j = emp[k]
            uid = (i//3)*3 + j//3
            for ch in map(str,range(1,10)):
                if ch not in row[i] and ch not in col[j] and ch not in sq[uid]:
                    b[i][j] = ch
                    row[i].add(ch)
                    col[j].add(ch)
                    sq[uid].add(ch)
                    if backtrack(k+1):
                        return True
                
                    b[i][j] = '.'
                    row[i].remove(ch)
                    col[j].remove(ch)
                    sq[uid].remove(ch)

            return False
        backtrack()



            
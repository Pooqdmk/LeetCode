class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        r=defaultdict(set)
        c=defaultdict(set)
        sq=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    continue
                
                if b[i][j] in r[i] or b[i][j] in c[j] or b[i][j] in sq[(i//3,j//3)]:
                    return False
                
                r[i].add(b[i][j])
                c[j].add(b[i][j])
                sq[(i//3,j//3)].add(b[i][j])
        return True
class Solution:
    def countCollisions(self, dir: str) -> int:
        n = len(dir)
        i,j = 0,n-1

        while i<n and dir[i] == 'L':
            i+=1
        
        while j>-1 and dir[j] == 'R':
            j-=1

        return sum(1 if dir[k]!='S' else 0 for k in range(i,j+1))
        
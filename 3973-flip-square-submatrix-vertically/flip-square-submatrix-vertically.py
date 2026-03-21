class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        res = [ i[y:y+k] for i in grid[x:x+k]]
        l,r = 0,k-1
        while l < r:
            t = res[l]
            res[l] = res[r]
            res[r] = t
            l+=1
            r-=1
        j = 0
        for i in grid[x:x+k]:
            i[y:y+k] = res[j]
            j+=1
        return grid
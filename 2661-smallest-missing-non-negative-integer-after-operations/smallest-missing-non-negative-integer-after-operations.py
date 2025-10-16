class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d ={}
        for i in nums:
            d[i%value] = d.get(i%value,0)+1
        
        i=0
        while True:
            cur = i%value
            if d.get(cur,0) == 0:
                return i 
            else:
                d[cur]-=1
            i+=1
        
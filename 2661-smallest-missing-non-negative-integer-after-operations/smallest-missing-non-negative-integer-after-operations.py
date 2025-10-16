class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d ={}
        for i in nums:
            d[i%value] = d.get(i%value,0)+1
        
        i=0
        while True:
            if i%value not in d or d[i%value] == 0:
                return i
            else:
                d[i%value]-=1
            i+=1
        
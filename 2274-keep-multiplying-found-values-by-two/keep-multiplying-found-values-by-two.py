class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        curr=o
        
        i=1
        while(1):
            if curr not in nums:
                return curr
            
            curr=curr*2
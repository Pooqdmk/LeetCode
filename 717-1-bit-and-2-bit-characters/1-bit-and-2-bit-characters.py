class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        n=len(bits)
        i=0
        while i < n:
            if bits[i]==1:
                i+=2
                
            else:
                if i==n-1 and bits[i]==0:
                    return True
                i+=1

        return False
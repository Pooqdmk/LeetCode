class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        if n == 1:
            return bits[-1] == 0
        while i < n-1:
            if bits[i] == 1:
                i+=2
            else:
                i+=1
            if i == n-1:
                return True
        
        return False
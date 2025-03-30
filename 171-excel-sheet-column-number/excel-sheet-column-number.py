class Solution:
    def titleToNumber(self, col: str) -> int:
        res=0
        for char in col:
            res=res*26+(ord(char)%ord('A')+1)

        return res
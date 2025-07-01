class Solution:
    def squareIsWhite(self, coord: str) -> bool:
        d={chr(i+96):i for i in range(1,9)}

        if d[coord[0]] % 2 == 0:
            return int(coord[1]) % 2 != 0
        
        else:
            return int(coord[1]) % 2 == 0

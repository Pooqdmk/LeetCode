class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = []
        n = len(bank)
        for i in range(n):
            b = bank[i].count('1')
            if b!=0:
                beams.append(b)
        res = 0
        for i in range(len(beams)-1):
            res+=beams[i]*beams[i+1]
        return res
        

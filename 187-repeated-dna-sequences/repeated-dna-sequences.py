class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        res = set()
        for i in range(len(s)-9):
            l = s[i:i+10]
            d[l] = d.get(l,0)+1
            if d[l] > 1:
                res.add(l)
        return list(res)

        
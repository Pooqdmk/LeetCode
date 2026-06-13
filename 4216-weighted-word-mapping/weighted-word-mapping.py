class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for i in words:
            s = 0
            for j in i:
                s+= weights[abs(97 - ord(j))]
            res.append(chr(122 - (s%26)))
        return ''.join(res)
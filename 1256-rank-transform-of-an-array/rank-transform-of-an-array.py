class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = list(sorted(set(arr)))
        d = {s[i]:i+1 for i in range(len(s))}
        res = []
        for i in arr:
            res.append(d[i])
        return res


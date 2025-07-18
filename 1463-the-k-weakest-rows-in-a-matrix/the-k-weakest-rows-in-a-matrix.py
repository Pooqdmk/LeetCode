class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l={}
        for i in range(len(mat)):
            l[i]=mat[i].count(1)

        d=dict(sorted(l.items(),key=lambda x:x[1]))

        return list(d.keys())[:k]
        

            
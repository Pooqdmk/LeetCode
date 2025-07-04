class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # d=sorted(set(arr))
        # res=[]
        # for i in arr:
        #     res.append(d.index(i)+1)
        # return res

        d={val:i+1 for i,val in enumerate(sorted(set(arr)))}
        res=[]
        for i in arr:
            res.append(d[i])
        return res

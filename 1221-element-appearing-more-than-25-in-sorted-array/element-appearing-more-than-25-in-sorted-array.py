class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d=Counter(arr)
        mx=-1
        res=0
        for key,val in d.items():
            c=mx
            mx=max(mx,val)
            if c != mx:
                res=key
        return res

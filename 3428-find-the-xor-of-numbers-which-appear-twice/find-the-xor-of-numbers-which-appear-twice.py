class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d=Counter(nums)
        res=[]
        for k,v in d.items():
            if v==2:
                res.append(k)
        c=0
        for i in res:
            c^=i
        return c
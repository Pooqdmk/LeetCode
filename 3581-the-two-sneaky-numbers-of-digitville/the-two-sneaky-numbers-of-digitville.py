class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        res = []
        for k,v in d.items():
            if v == 2:
                res.append(k)
            if len(res) == 2:
                break
        return res

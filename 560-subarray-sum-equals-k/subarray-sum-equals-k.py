class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        pre = 0
        res = 0
        for i in nums:
            pre+=i
            if pre == k:
                res+=1
            rem = pre - k
            if rem in d:
                res+= d[rem]
            d[pre] = d.get(pre,0)+1
        print(d)
        return res



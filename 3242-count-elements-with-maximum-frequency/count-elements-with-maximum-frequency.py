class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        l=list(d.values())
        l.sort(reverse=True)
        mx=l[0]
        res=0
        for i in range(len(l)):
            if mx == l[i]:
                res+=mx
            else:
                break
        return res

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for val in nums:
            d[val]=d.get(val,0)+1
        l=list(d.values())
        mx=0
        res=0
        for i in l:
            prev=mx
            mx=max(mx,i)
            if i == mx:
                res+=i
            if prev!=mx:
                res=i
        return res

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if rem == 0:
            return 0
        d = {0:-1}
        s = 0
        mn = 10**60
        for i,n in enumerate(nums):
            s = (s+n)%p
            m = (s - rem +p)%p
            if m in d:
                mn = min(mn,i-d[m])
            d[s] = i
        return mn if mn!= 10**60 and mn!=len(nums) else -1

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        mx = floor(sum(nums)/len(nums))
        seen = set(nums)
        mx=max(1,mx+1)
        while True:
            if  mx not in seen:
                return mx

            mx+=1

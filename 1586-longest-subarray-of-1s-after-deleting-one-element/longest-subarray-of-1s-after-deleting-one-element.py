class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=[]

        for i in range(len(nums)):
            if nums[i] == 0:
                l.append(i)

        mx=0
        n=len(l)
        if n == 1:
            mx=max(mx,nums[:l[0]].count(1)+nums[l[0]+1:].count(1))
        if n>1:
            mx=max(mx,nums[:l[0]].count(1)+nums[l[0]+1:l[1]].count(1))
            for i in range(1,n-1):
                mx=max(mx,nums[l[i-1]+1:l[i+1]].count(1))
            mx=max(mx,nums[l[-2]+1:].count(1))
        if n==0:
            return nums.count(1)-1
        return mx

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i<0:
                l.append(i)
        l.sort()
        b=0
        if len(l)>=2:
            b=l[0]*l[1]
        nums.sort()
        n=len(nums)
        m=nums[n-1]*nums[n-2]*nums[n-3]
        if n==3:
            return m
        if m>(b*nums[n-1]):
            return m
        else:
            return b*nums[n-1]

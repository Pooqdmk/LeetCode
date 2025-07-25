class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set(nums)
        p=0
        n=[]
        for i in s:
            if i>0:
                p+=i
            elif i<0:
                n.append(i)
        if p>0:
            return p
        else:
            if 0 in s:
                return 0
            else:
                n.sort(reverse=True)
                return n[0]

        
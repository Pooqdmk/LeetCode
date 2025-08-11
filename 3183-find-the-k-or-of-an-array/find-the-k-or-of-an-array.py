class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        l=len(bin(mx)[2:])
        res=[0]*l
        for i in nums:
            n=bin(i)[2:].zfill(l)
            for j in range(l):
                if n[j] == '1':
                    res[j]+=1
        
        r=['0']*l
        for i in range(len(res)):
            if res[i]>=k:
                r[i]='1'
        return int(''.join(r),2)
            

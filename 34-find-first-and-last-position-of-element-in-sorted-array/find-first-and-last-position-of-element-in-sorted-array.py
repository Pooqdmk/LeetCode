class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        l=[-1]*2
        a=len(nums)
        e=a-1
        
        while s<a:
            if nums[s]==target:
                l[0]=s
                break
            s+=1
        while e>=0:
            if nums[e]==target:
                l[1]=e
                break
            e-=1  
        return l    
               

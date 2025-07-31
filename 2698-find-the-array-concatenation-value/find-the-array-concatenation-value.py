class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        res=0
        while left<right:
            s=str(nums[left])+str(nums[right])
            res+=int(s)
            left+=1
            right-=1
        if left == right:
            res+=nums[left]
        return res        
        
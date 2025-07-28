class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            res=[]
            n=len(nums)
            for i in range(0,n,4):
                res.append(min(nums[i],nums[i+1]))
                if i+2 < n and i+3 < n:
                    res.append(max(nums[i+2],nums[i+3]))
                
            nums=res

        return nums[-1]
            

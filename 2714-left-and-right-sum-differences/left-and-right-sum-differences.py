class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls,rs=0,sum(nums)-nums[0]
        res=[]
        for i in range(1,len(nums)):
            res.append(abs(ls-rs))
            
            ls+=nums[i-1]
            
            rs-=nums[i]
        res.append(abs(ls-rs))
        return res



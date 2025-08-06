class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls,rs=0,0
        res=[]
        for i in range(len(nums)):
            if len(nums[:i])>0:
                ls=sum(nums[:i])
            if len(nums[i+1:])>0:
                rs=sum(nums[i+1:])
            else:
                rs=0

            res.append(abs(ls-rs))
        return res



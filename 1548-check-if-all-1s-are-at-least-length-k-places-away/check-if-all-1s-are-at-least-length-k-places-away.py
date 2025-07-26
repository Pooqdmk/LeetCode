class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        res=[]

        for i in range(len(nums)):
            if nums[i] == 1:
                res.append(i)

        for i in range(len(res)-1):
            if res[i+1]-res[i]<=k:
                return False

        return True

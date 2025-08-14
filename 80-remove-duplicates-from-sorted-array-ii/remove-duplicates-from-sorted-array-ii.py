class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        d=Counter(nums)
        res=[]
        for k,v in d.items():
            if v<=2:
                res+=[k]*v
            else:
                res+=[k]*2
        nums[:]=res

        # for i in nums:
        #     if d[i] > 2:
        #         while d[i] > 2:
        #             nums.remove(i)
        #             d[i]-=1
        
        return len(nums)
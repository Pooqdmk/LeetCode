class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        for key,val in d.items():
            if val==2:
                m=key
                break
        # if m-1 not in nums and m-1>0 :
        #     return [m,m-1]
        # else:
        #     return [m,m+1]

        for i in range(1,len(nums)+1):
            if i not in nums:
                return [m,i]

        

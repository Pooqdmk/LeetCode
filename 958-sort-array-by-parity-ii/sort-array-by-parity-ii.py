class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        o=[]
        e=[]
        for i in nums:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        res=[]
        for i in range(len(nums)//2):
            res.append(e[i])
            res.append(o[i])
        return res
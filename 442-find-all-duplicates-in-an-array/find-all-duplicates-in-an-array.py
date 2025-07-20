class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        res=[]
        for key,val in d.items():
            if val==2:
                res.append(key)

        return res
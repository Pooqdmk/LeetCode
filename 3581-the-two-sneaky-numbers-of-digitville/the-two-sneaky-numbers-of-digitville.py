class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0)+1
        # res = []
        # for k,v in d.items():
        #     if v == 2:
        #         res.append(k)
        #     if len(res) == 2:
        #         break
        # return res
        nums.sort()
        i=0
        res = []
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                i+=2
            elif len(res) == 2:
                return res
            else:
                i+=1
        return res


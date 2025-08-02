class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] == key:
                if i+1<len(nums):
                    d[nums[i+1]]=d.get(nums[i+1],0)+1
        l=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
        return l[0][0]
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d=Counter(nums)
        cnt=0
        for key,val in d.items():
            if val>1:
                cnt+=((val)*(val-1))//2
        return cnt
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx=max(nums)

        d=Counter(nums)
        for i in range(1,mx):
            if i in nums and d[i]==1:
                continue
            else:
                return False
        return d[mx]==2


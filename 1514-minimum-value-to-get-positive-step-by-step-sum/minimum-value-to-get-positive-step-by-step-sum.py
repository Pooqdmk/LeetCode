class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre=0
        mn=0
        for i in nums:
            pre+=i
            mn=min(mn,pre)

        return 1-mn
    
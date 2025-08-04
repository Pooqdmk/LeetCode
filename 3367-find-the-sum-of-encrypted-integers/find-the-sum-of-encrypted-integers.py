class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            s=str(i)
            mx=max(s)
            l=[mx]*len(s)
            res+=int(''.join(l))
        return res
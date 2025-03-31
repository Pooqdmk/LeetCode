class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        m=0
        for i in  nums:
            cnt+=i
            m=max(m,cnt)
            if i==0:
                cnt=0
        return m
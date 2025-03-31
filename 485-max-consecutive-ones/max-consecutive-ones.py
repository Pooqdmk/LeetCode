class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maximum=0
        for i in  nums:
            cnt+=i
            maximum=max(maximum,cnt)
            if i==0:
                cnt=0
        return maximum
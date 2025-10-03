class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in d:
                d[s%k] = i
            else:
                if i - d[s%k] > 1:
                    return True
        return False

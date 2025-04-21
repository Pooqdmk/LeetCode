class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        cnt=0
        for key,val in d.items():
            if key==k:
                continue
            if key<k:
                return -1
            else:
                cnt+=1
        return cnt
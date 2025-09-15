class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        res=set()
        for i in range(len(nums)):
            if k == 0:
                break
            prev =len(res)
            res.add(nums[i])
            if len(res) != prev:
                k-=1
        return sorted(list(res),reverse=True)
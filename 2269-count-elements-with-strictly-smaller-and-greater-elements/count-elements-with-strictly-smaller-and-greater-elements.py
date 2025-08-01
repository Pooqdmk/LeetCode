class Solution:
    def countElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        nums=set(nums)
        nums= sorted(nums)
        cnt=0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] > nums[i]:
                cnt+=d[nums[i]]
        return cnt

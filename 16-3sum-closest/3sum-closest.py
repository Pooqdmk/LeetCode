class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = -10000
        mn = 10**60
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                prev = mn
                mn = min(mn,abs(target-s))
                if prev != mn:
                    res = s
                if s < target:
                    l+=1
                else:
                    r-=1
        return res

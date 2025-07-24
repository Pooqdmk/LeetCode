class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_incr(a):
            return all(a[i]<a[i+1] for i in range(len(a)-1))
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                
                a=nums[:i]+nums[i+1:]
                b=nums[:i+1]+nums[i+2:]

                return is_incr(a) or is_incr(b)
        return True

        
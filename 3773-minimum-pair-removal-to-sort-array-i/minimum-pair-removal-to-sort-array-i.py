class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            is_sorted = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    is_sorted= False
                    break 
            if not is_sorted:
                cnt+=1
                mn = 10**60
                idx = -1
                for i in range(len(nums)-1):
                    if nums[i] + nums[i+1] < mn:
                        mn = nums[i]+nums[i+1]
                        idx = i
                
                l = nums[:idx] + [mn] + nums[idx+2:]
                nums = l
            else:
                return cnt
        return cnt


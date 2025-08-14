class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        d=Counter(nums)
        for i in nums:
            if d[i] > 2:
                while d[i] > 2:
                    nums.remove(i)
                    d[i]-=1
        
        return len(nums)
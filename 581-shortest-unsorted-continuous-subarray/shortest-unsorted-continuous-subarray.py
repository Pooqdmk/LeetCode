class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = sorted(nums)
        s,e = -1,-1
        for i in range(len(nums)):
            if nums[i] != l[i]:
                s = i
                break
        
        for i in range(s+1,len(nums)):
            if nums[i] != l[i]:
                e = i

        print(s, e)
        return e - s + 1 if e-s!=0 else 0
            
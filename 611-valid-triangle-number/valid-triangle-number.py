class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        k=len(nums)-1
        res=0
        while k > 1:
            l,h=0,k-1
            while l<h:
                if nums[l] + nums[h] > nums[k]:
                    res+=h-l
                    h-=1
                else:
                    l+=1
            k-=1
        return res


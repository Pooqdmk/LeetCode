class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        seen=set()
        s=0
        l=0
        mx=-1
        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[l])
                s-=nums[l]
                l+=1
            seen.add(nums[i])
            s+=nums[i]
            mx=max(mx,s)
        return mx

        
        
        
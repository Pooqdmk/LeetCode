class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
       
        mx=0
        for i in range(0,n):
            if nums[i]%2==0 and nums[i]<= threshold:
                cnt=1
                for j in range(i+1,n):
                    if nums[j]>threshold or nums[j]%2 == nums[j-1]%2:
                        break
                    cnt+=1
                mx=max(mx,cnt)
                                
        
        return mx
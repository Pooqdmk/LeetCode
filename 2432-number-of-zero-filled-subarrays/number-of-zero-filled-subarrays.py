class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        i=0
        while i < (len(nums)):
            if nums[i]==0:
                cnt=1
                for j in range(i+1,len(nums)):
                    if nums[j]==0:
                        cnt+=1
                    else:
                        break
                
                res+=((cnt)*(cnt+1))//2 
                i+=cnt
            else:
                i+=1
        return res
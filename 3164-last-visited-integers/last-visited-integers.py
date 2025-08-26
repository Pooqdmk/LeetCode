class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen=[]
        ans=[]
        cnt=0
        for i in range(len(nums)):
            if nums[i]!=-1:
                seen.insert(0,nums[i])
                cnt=0
            else:
                cnt+=1
                if cnt<=len(seen):
                    ans.append(seen[cnt-1])
                else:
                    ans.append(-1)
        return ans
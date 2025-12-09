class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        cnt = 0
        l,r = {nums[0]:1},{}
        for i in range(1,len(nums)):
            r[nums[i]] = r.get(nums[i],0)+1
        
        for i in range(1,len(nums)-1):
            r[nums[i]] -=1
            t = nums[i]*2
            if t in l and l[t] > 0 and t in r and r[t] > 0:
                cnt+=l[t]*r[t]
            l[nums[i]] = l.get(nums[i],0)+1
            
        return cnt%((10**9) + 7)

                

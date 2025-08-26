class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        d=Counter(nums)
        # l=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
        mx=max(d.values())
        cnt=0
        for i,j in d.items():
            if j==mx:
                cnt+=j
            
        return cnt

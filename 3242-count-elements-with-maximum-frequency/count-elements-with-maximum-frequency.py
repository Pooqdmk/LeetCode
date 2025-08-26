class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        d=Counter(nums)
        l=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
        mx=l[0][1]
        cnt=0
        for i,j in l:
            if j==mx:
                cnt+=j
            else:
                break
        return cnt

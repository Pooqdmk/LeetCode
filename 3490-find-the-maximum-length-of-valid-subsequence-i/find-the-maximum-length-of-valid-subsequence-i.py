class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        o,e=0,0
        for i in nums:
            if i%2==0:
                e+=1
            else:
                o+=1
        
        toggle=True
        cnt=0
        for i in nums:
            prev=toggle
            if i%2==0:
                toggle=False
            else:
                toggle=True
            if prev!=toggle:
                cnt+=1
        toggle=True
        cnt1=0
        for i in nums:
            prev=toggle
            if i%2!=0:
                toggle=False
            else:
                toggle=True
            if prev!=toggle:
                cnt1+=1

        return max(cnt1,cnt,o,e)

        
            
        


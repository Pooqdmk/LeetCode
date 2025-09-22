class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right,mx= 0,0,0
        d={}
        while right< len(s):
            d[s[right]]=d.get(s[right],0)+1
            m=max(d.values())
            while (right-left+1) - m > k:
                d[s[left]]=d.get(s[left])-1
                left+=1
                
            mx=max(mx,right-left+1)
            right+=1
        return mx

            
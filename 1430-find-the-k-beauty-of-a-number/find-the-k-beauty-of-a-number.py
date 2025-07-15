class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        cnt=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                l=s[i:j]
                
                if len(l) == k and l.lstrip('0')!='' and num % int(l.lstrip('0'))==0:
                    cnt+=1
        return cnt
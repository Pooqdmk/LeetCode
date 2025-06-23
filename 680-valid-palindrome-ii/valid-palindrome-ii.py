class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if s == s[::-1]:
        #     return True
        start=0
        end=len(s)-1
        while start<end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                r=s[start+1:end+1]
                t=s[start:end]
                return t==t[::-1] or r==r[::-1]
                    
                
        return True


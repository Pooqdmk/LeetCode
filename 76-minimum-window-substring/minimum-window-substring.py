class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT,window = {},{}
        for i in t:
            countT[i] = countT.get(i,0)+1

        have,need = 0,len(countT)
        res,mn = [-1,-1],10**60

        l=0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have+=1
            
            while have == need:
                if mn> (r-l+1):
                    mn = r-l+1
                    res = [l,r]

                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1

                l+=1
        return s[res[0]:res[-1]+1]

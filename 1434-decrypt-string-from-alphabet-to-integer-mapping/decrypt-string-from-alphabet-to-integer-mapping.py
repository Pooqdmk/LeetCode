class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={str(i):chr(i+96) for i in range(1,27)}
        # l={str(i)+'#':chr(i+96) for i in range(10,27)}

        res=''
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                res+=d[s[i:i+2]]
                i+=3
            else:
                res+=d[s[i]]
                i+=1
        return res
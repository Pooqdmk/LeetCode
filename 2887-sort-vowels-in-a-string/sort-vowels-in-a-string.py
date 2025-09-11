class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        for i,ch in enumerate(s):
            if ch.lower() in 'aeiou':
                l.append([i,ch])
        
        d=sorted(ch[1] for ch in l)
        res=[]
        j=0
        for i,ch in enumerate(s):
            if ch.lower() not in 'aeiou':
                res.append(ch)
            else:
                res.append(d[j])
                j+=1
        return ''.join(res)
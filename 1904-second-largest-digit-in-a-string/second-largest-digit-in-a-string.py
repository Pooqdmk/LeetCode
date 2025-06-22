class Solution:
    def secondHighest(self, s: str) -> int:
        
        l=[]
        for i in s:
            if i.isdigit() and i not in l:
                l.append(i)
        if len(l)>=2:
            l.sort()
            return int(l[-2])
        else:
            return -1
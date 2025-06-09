class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start=0
        end=len(s)
        l=[]
        for i in s:
            if i=='I':
                l.append(start)
                start+=1
            else:
                l.append(end)
                end-=1
        for i in range(end+1):
            if i not in l:
                l.append(i)
        return l

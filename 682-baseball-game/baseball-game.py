class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i.lstrip('-').isdigit():
                l.append(int(i))
            elif i=='+':
                l.append(l[-1]+l[-2])
            elif i=='D':
                l.append(l[-1]*2)
            elif i=='C':
                l.pop()
        return sum(l)


            
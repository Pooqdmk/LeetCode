class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt=0
        for i in text:
            if i==' ':
                cnt+=1        
        t=text.split()  
        l=len(t)

        if l==1:
            return t[-1]+' '*cnt

        div=cnt//(l-1)
        m=cnt % (l-1)
        res=''
        for i in range(len(t)-1):
            res+=t[i]+' '*div

        res+=t[-1]

        return res+' '*m


        
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        key=key.replace(' ','')
        d={}
        j=0
        for i in key:
            if i not in d:
                d[i]=chr(j+97)
                j+=1
        res=''
        for i in message:
            if i != ' ':
                res+=d[i]
            else:
                res+=i
        return res
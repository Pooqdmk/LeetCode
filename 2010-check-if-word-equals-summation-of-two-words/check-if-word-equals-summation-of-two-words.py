class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        d={chr(i+97):str(i) for i in range(0,26)}
        res=''
        for i in firstWord:
            res+=d[i]
        res=int(res)
        res2=''
        for i in secondWord:
            res2+=d[i]
        res2=int(res2)
        res3=''
        for i in targetWord:
            res3+=d[i]
        res3=int(res3)
        return res+res2 == res3
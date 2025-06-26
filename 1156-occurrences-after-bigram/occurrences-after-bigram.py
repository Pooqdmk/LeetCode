class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l=text.split(' ')
        res=[]
        for i in range(len(l)-2):
            if l[i]==first and l[i+1]==second:
                res.append(l[i+2])
        return res

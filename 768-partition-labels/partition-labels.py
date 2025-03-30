class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={char:i for i,char in enumerate(s)}
        l=[]
        end=0
        start=0
        for i,char in enumerate(s):
            end=max(end,d[char])

            if i==end:
                l.append(i-start+1)
                start=i+1
        return l
            

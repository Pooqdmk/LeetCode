class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # b=(len(s)%10) *10
        # a=ceil(len(s)/10)

        d={chr(i+ord('a')):widths[i] for i in range(len(widths))}
        sum=0
        cnt=1
        for i in s:
            if sum+d[i]<=100:
                sum=sum+d[i]
            else:
                sum=d[i]
                cnt=cnt+1
        return [cnt,sum]
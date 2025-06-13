class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x)[2:]
        b=bin(y)[2:]

        l=len(a)
        m=len(b)

        if l<m:
            a='0'*(m-l)+a
        else:
            b='0'*(l-m)+b


        cnt=0
        for i in range(len(a)):
            if (a[i]=='1' and b[i]=='0') or (a[i]=='0' and b[i]=='1'):
                cnt+=1
        
        return cnt

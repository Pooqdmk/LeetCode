class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1)+int(num2))
        i=len(num1)-1
        j=len(num2)-1
        res=[]
        carry=0
        while i>=0 or j>=0 or carry:
            digit1=int(num1[i]) if i>=0 else 0
            digit2=int(num2[j]) if j>=0 else 0
            tot=digit1+digit2+carry
            carry=tot//10
            res.append(str(tot%10))
            i-=1
            j-=1
        return ''.join(res[::-1])

       
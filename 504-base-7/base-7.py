class Solution:
    def convertToBase7(self, num: int) -> str:
        # return int(num,7)
        s=''
        if num<0:
            n=int(str(num)[1:])
        elif num>0:
            n=num
        else:
            return "0"
        while(n>0):
            rem=n%7
            s+=str(rem)
            n=n//7
        if num<0:
            return '-'+s[::-1]
        else:
            return s[::-1]

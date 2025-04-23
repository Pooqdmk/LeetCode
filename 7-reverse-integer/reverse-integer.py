class Solution:
    def reverse(self, x: int) -> int:
        try:
            y=str(x)
            if y[0]!='-':
                res= int(y[::-1].lstrip('0'))
            else:
                res= int(y[0]+y[1:][::-1].lstrip('0'))
            if res<-2**31 or res>2**31-1:
                return 0
            return res
        except:
            return 0
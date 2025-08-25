class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res=''

        while a>0 or b>0:
            if a>b:
                if len(res)>1 and res[-1] == res[-2] == 'a':
                    res+='b'
                    b-=1
                else:
                    res+='a'
                    a-=1

            else:
                if len(res)>1 and res[-1] == res[-2] == 'b':
                    res+='a'
                    a-=1
                else:
                    res+='b'
                    b-=1
        return res

            
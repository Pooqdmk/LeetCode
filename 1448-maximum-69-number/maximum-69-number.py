class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        res=''
        i=0
        while i < len(s):
            if s[i] == '6':
                res+='9'
                i+=1
                break
            else:
                res+=s[i]
                i+=1
        while i<len(s):
            res+=s[i]
            i+=1
        return int(res)


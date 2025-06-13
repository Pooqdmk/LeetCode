class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num)[2:]
        m=''
        for i in (n):
            if i=='0':
                m+='1'
            else:
                m+='0'
        return int(m,2)

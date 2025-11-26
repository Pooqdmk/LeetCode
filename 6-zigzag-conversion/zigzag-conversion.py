class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ''
        for i in range(numRows):
            incr = (numRows-1)*2
            for j in range(i,len(s),incr):
                res+=s[j]

                if i>0 and i<numRows-1 and j+incr-2*i < len(s):
                    res+=s[j+incr-2*i]
        return res

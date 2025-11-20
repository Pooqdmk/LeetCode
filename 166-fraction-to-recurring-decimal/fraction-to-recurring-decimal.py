class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return '0'
        res = []
        if (n < 0 and d>0) or (d < 0 and n>0):
            res.append('-')
        n,d = abs(n),abs(d)
        res.append(str(n//d))
        rem = n%d
        if rem == 0:
            return ''.join(res)
        res.append('.')
        l = {}

        while rem != 0:
            if rem in l:
                pos = l[rem]
                res.insert(pos,'(')
                res.append(')')
                return ''.join(res)

            l[rem] = len(res)
            rem*=10
            res.append(str(rem//d))
            rem%=d
        return ''.join(res)
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        r=s.replace('-','').upper()
        res=[]
        # for i in range(len(r)):
        while len(r)>k:
            res.append(r[-k:])
            r=r[:-k]
        if r:
            res.append(r)

        return '-'.join(res[::-1])            


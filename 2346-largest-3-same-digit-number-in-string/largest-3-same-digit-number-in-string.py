class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx=-1
        for i in range(len(num)-2):
            s=num[i:i+3]
            if len(set(s)) == 1:
                mx=max(mx,int(s))
        return str(mx).zfill(3) if mx!=-1 else ""
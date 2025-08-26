class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        for i in range(len(s)):
            if s[i].isdigit():
                size*=int(s[i])
            else:
                size+=1

        for i in reversed(s):
            if i.isdigit():
                size//=int(i)
                k%=size
            else:
                if k==size or k==0:
                    return i
                size-=1
        
                
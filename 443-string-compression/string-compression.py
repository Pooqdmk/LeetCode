class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt=1
        res=[]
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                cnt+=1
            else:
                res.append(chars[i])
                if cnt>1:
                    for i in str(cnt):
                        res.append(i)
                cnt=1
        res.append(chars[-1])
        if cnt>1:
            for i in str(cnt):
                res.append(i)
        chars[:]=res
        return len(chars)


        


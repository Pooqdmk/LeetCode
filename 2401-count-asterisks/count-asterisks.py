class Solution:
    def countAsterisks(self, s: str) -> int:
        # l=[]
        # for i in range(len(s)):
        #     if s[i] == '|':
        #         l.append(i)
        # res=[]
        # for i in range(0,len(l),2):
        #     res.append(s[l[i]:l[i+1]+1])

        # for i in res:
        #     s=s.replace(i,'')
        # cnt=0
        # for i in s:
        #     if i=='*':
        #         cnt+=1
        # return cnt

        inside =False
        cnt=0
        for i in s:
            if i == '|':
                inside = not inside

            elif i == '*' and not inside:
                cnt+=1
        return cnt


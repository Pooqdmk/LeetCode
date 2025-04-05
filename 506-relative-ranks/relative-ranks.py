class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        d={}
        for i in range(len(s)):
            if i==0:
                d[s[i]]="Gold Medal"
            elif i == 1:
                d[s[i]] = "Silver Medal"
            elif i == 2:
                d[s[i]] = "Bronze Medal"
            else:
                d[s[i]] = str(i + 1)

        # d={s[0]:"Gold Medal",s[1]:"Silver Medal",s[2]:"Bronze Medal"}
        # k=4
        # for i in range(3,len(s)):
        #     d[s[i]]=str(k)
        #     k+=1
        li=[]
        for i in score:
            li.append(d[i])
        return li
            

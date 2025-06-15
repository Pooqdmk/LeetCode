class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        # l=sorted(d.values(),reverse=True)
        # i=0
        # res=''
        # for key in d.keys():
        #     if d[key]==l[i]:
        #         res+=key*l[i]
        #         i+=1

        s=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
        res=''
        for key,val in s.items():
            res+=key*val
        return res



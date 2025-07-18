class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d={}

        for i in dominoes:
            # if tuple(i) not in d and tuple(i[::-1]) not in d:
            #     d[tuple(i)]=1
            # else:
            #     if tuple(i) in d:
            #         d[tuple(i)]+=1
            #     else:
            #         d[tuple(i[::-1])]+=1
            key=tuple(sorted(i))
            d[key]=d.get(key,0)+1

        cnt=0
        for key,val in d.items():
            if val>1:
                cnt+=(val)*(val-1)//2

        return cnt


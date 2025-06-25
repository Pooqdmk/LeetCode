class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        # start=0
        # end=len(s)-1
        # while start<end:
        #     if s[start] == s[end]:
        #         return len(s[start+1:end])
        #     start+=1
        #     end-=1
        # return -1

        d=defaultdict(list)

        for i in range(len(s)):
            # if s[i] not in d:
            d[s[i]].append(i)

        mx=-1
        for key,val in d.items():
            if len(val) >=2:
                # val.sort()
                mx=max(mx,val[-1]-val[0]-1)

        return mx

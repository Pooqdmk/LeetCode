class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        d = defaultdict(list) #business: (code,isActive)
        n = len(code)
        seen = set([ "electronics", "grocery", "pharmacy", "restaurant"])
        for i in range(n):
            if businessLine[i] in seen and code[i] != '' and isActive[i] == True:
                d[businessLine[i]].append(code[i])

        l = sorted(d.items(),key = lambda x: x[0])
        print(l)
        res =[]
        for k,v in l:
            v.sort()
            for j in v:
                valid = True
                for i in j:
                    if i.isalnum() or i == '_':
                        continue
                    else:
                        valid = False
                        break
                if valid:
                    res.append(j)
        return res

            

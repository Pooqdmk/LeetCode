class Solution:
    def maxFreqSum(self, s: str) -> int:
        v,c='',''
        for i in s:
            if i in 'aeiou':
                v+=i

            else:
                c+=i
        
        m=Counter(v)
        n=Counter(c)
        y=list(m.values())
        z=list(n.values())
        if y and z:
            return max(y)+max(z)
        elif y:
            return max(y)
        else:
            return max(z) 

                

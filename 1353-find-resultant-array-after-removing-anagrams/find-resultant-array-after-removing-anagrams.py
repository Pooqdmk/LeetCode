class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        

        
        while True:
            i=0
            found = False
            while i < len(words)-1:

                a = words[i]
                b = words[i+1]
                d,l = {},{}
                if len(a) == len(b):
                    for j in range(len(a)):
                        d[a[j]] = d.get(a[j],0)+1
                        l[b[j]] = l.get(b[j],0)+1
                    if d == l:
                        found = True
                        words[:] = words[:i+1]+words[i+2:]
                        break
                i+=1
            if not found:
                break
        return words


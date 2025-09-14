class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def dovowel(i):
            vowels = {'a','e','i','o','u'}
            res = []
            for j in i:
                if j in vowels:
                    res.append('*')
                else:
                    res.append(j)
            return ''.join(res)

        d=defaultdict(list)
        l=defaultdict(list)
        for i in wordlist:
            d[i.lower()].append(i)
            l[dovowel(i.lower())].append(i)
            

        res=[]
        words = set(wordlist)
        for i in queries:
            if i in words:
                res.append(i)
            
            
            elif i.lower() in d:
                res.append(d[i.lower()][0])
                
            
            else:
                if dovowel(i.lower()) in l:
                    res.append(l[dovowel(i.lower())][0])
                else:
                    res.append('')
        return res
                
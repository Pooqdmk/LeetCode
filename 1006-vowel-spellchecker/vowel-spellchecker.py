class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def dovowel(word):
            return ''.join('*' if c.lower() in 'aeiou' else c.lower() for c in word )

        l={}
        v={}
        words=set(wordlist)
        for i in wordlist:
            lower=i.lower()
            vowel=dovowel(i)
            if lower not in l:
                l[lower]=i
            if vowel not in v:
                v[vowel]=i
        
        res=[]
        for i in queries:
            if i in words:
                res.append(i)

            elif i.lower() in l:
                res.append(l[i.lower()])
            elif dovowel(i) in v:
                res.append(v[dovowel(i)])
            else:
                res.append('')
        return res
            

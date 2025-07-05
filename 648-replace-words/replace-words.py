class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        d={}
        l=sentence.split()
        for i in l:
            for j in dictionary:
                if i in d:
                    break
                if i.startswith(j):
                    d[i] = j
                    break

        for i in range(len(l)):
            if l[i] in d:
                l[i]=d[l[i]]
        return ' '.join(l)


class Solution:
    def isValid(self, word: str) -> bool:
        n=len(word)
        if n<3:
            return False
        c,v=0,0
        word=word.lower()
        for i in word:
            if i.isdigit():
                continue
            elif i.isalpha():
                if i in 'aeiou':
                    v+=1
                else:
                    c+=1
            else:
                return False
        if v>=1 and c>=1:
            return True
        
        return False

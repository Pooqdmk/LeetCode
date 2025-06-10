class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l=sentence.split(' ')
        # cnt=2
        for i in range(len(l)):
            if l[i][0] not in "aeiou" and l[i][0] not in "AEIOU":
                l[i]=l[i][1:]+l[i][0]+"ma"+"a"*(i+1)
                # cnt+=1
            else:
                l[i]=l[i]+"ma"+"a"*(i+1)
        return ' '.join(l)
                

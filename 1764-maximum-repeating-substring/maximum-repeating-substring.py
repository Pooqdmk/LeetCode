class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # i=0
        # l=len(word)
        # cnt=0
        # while i<len(sequence):
        #     if sequence[i:i+l] == word:
        #         i+=l
        #         cnt+=1
        #     else:
        #         i+=1
        # return cnt

        s=len(sequence)
        w=len(word)
        m= s//w
        while m >= 0:
            if m * word in sequence:
                return m
            m-=1
        return 0
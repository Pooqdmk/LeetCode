class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        while(1):
            res=''
            for i in word:
                res+=chr(ord(i)+1)
            
            word+=res
            if len(word) >=k:
                return word[k-1]
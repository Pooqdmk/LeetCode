class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        s=''
        for i in licensePlate:
            if i.isalpha():
                s+=i.lower()
        
        req=Counter(s)
        words.sort(key=len)
        for i in words:
            mat=Counter(i)
            if all(mat[char]>=req[char] for char in req):
                return i
        return ""
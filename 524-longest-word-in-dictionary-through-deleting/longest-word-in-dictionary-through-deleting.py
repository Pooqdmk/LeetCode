class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        mx = 0
        for word in dictionary:
            stack = []
            i,j = 0,0
            n = len(word)
            while i < n and j<len(s):
                if s[j] == word[i]:
                    stack.append(s[j])
                    i+=1
                    j+=1
                else:
                    j+=1
            if ''.join(stack) == word:
                if n > mx:
                    mx = n
                    res = word
                elif n == mx:
                    if res > word:
                        res = word
        return res



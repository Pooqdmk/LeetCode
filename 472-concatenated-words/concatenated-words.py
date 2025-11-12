class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        res = []
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1,len(word)):
                pre = word[:i]
                suf = word[i:]

                if pre in seen and (suf in seen or dfs(suf)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        
        for i in words:
            if dfs(i):
                res.append(i)
        return res

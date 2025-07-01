class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1

        # d=Counter(word)

        # for i in d.values():
        #     cnt+=i-1

        # return cnt

        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                cnt+=1

        return cnt

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        i=0
        while i < len(words):
            if stack and Counter(stack[-1]) == Counter(words[i]):
                i+=1
            else:
                stack.append(words[i])
                i+=1
        return stack

        # res=[words[0]]

        # for i in range(1,len(words)):
        #     if Counter(words[i]) != Counter(res[-1]):
        #         res.append(words[i])
        # return res
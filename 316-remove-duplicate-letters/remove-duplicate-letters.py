class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        d={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in d:
                d[s[i]]=i
        in_stack = set()
        for i in range(len(s)):
            if s[i] in in_stack:
                continue

            while stack and stack[-1] > s[i] and d[stack[-1]]>i :
                in_stack.remove(stack.pop())
                
            stack.append(s[i])
            in_stack.add(s[i])

        return ''.join(stack)
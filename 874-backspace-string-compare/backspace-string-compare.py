class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            stack=[]
            for i in s:
                if i=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        if process(s)==process(t):
            return True
        else:
            return False

        
        
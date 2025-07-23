class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score=0
        if x>y:
            stack=[]
            for i in range(len(s)):
                if stack and stack[-1] == 'a' and s[i]=='b':
                    stack.pop()
                    score+=x
                else:
                    stack.append(s[i])
            s=''.join(stack)
            stack=[]
            for i in s:
                if stack and stack[-1]=='b' and i=='a':
                    stack.pop()
                    score+=y
                else:
                    stack.append(i)
            return score
        else:
            stack=[]
            for i in range(len(s)):
                if stack and stack[-1] == 'b' and s[i]=='a':
                    stack.pop()
                    score+=y
                else:
                    stack.append(s[i])
            s=''.join(stack)
            stack=[]
            for i in s:
                if stack and stack[-1]=='a' and i=='b':
                    stack.pop()
                    score+=x
                else:
                    stack.append(i)
            return score


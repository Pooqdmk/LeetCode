class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # cnt=0
        # for i in moves:
        #     if i=="U" or i=="R":
        #         cnt+=1
        #     else:
        #         cnt-=1
        # return True if cnt==0 else False

        # stack=[]

        # for i in moves:
        #     if stack and stack[-1]=="R" and i=="L":
        #         stack.pop()
        #     elif stack and stack[-1]=="L" and i=="R":
        #         stack.pop()
        #     elif stack and stack[-1]=="D" and i=="U":
        #         stack.pop()
        #     elif stack and stack[-1]=="U" and i=="D":
        #         stack.pop()
        #     else:
        #         stack.append(i)
        # return len(stack)==0
        r=l=d=u=0
        for i in moves:
            if i=="R":
                r+=1
            elif i=="L":
                l+=1
            elif i=="U":
                u+=1
            else:
                d+=1
        return (r==l) and (u==d)
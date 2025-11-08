class Solution:
    def calculate(self, s: str) -> int:
        
        i = 0
        res = 0
        curr_oper = '+'
        cur,prev = 0,0
        while i < len(s):
            curr_char = s[i]
            if curr_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur=cur*10 + int(s[i])
                    i+=1
                i-=1

                if curr_oper == '+':
                    res+=cur
                    prev = cur
                elif curr_oper == '-':
                    res-=cur
                    prev = -cur
                elif curr_oper == '*':
                    res-=prev
                    res+=cur*prev
                    prev = prev*cur
                else:
                    res-=prev
                    res+=int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif curr_char!= ' ':
                curr_oper = curr_char
            i+=1
        return res

                
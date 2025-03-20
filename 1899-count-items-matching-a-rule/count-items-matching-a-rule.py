class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt=0
        for i in items:
            if ruleKey=="color":
                if i[1]==ruleValue:
                    cnt=cnt+1
            elif ruleKey=="type":
                if i[0]==ruleValue:
                    cnt=cnt+1
            else:
                if i[2]==ruleValue:
                    cnt=cnt+1
        return cnt
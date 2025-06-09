class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        if s==goal:
            return len(set(s)) < len(s)
        l=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                l.append(i)

        if len(l)==2:
            i,j=l
            return s[i]==goal[j] and s[j]==goal[i]
        return False
            
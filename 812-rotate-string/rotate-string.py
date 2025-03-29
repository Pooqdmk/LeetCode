class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # i=s.find(goal[0])
        # if goal==s[i:]+s[:i]:
        #     return True
        # else:
        #     return False

        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False
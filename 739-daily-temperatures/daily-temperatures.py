class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n=len(t)
        ans=[0]*n

        stack=[]
        for i in range(n):
            while stack and t[stack[-1]] < t[i]:
                ans[stack.pop()] = i - stack[-1]
            
            stack.append(i)
        return ans


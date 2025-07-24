class Solution:
    def average(self, s: List[int]) -> float:
        # s=sum(salary)
        # return (s-min(salary)-max(salary))/(len(salary)-2)
        s.sort()
        return sum(s[1:-1])/(len(s)-2)
class Solution:
    def average(self, salary: List[int]) -> float:
        s=sum(salary)
        return (s-min(salary)-max(salary))/(len(salary)-2)
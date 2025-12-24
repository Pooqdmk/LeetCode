class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        capacity.sort(reverse = True)
        s = capacity[0]
        # cnt = 1
        for i in range(1,len(capacity)):
            if s >= n:
                return i
            s+=capacity[i]
        return len(capacity)



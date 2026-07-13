class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        for i in range(9):
            for j in range(i+1,10):
                t = int(s[i:j])
                if low <= t and t <= high:
                    res.append(t)
        return sorted(res)

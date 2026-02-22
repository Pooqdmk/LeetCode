class Solution:
    def binaryGap(self, n: int) -> int:
        m = list(bin(n)[2:])
        prev = -1
        gap = 0
        for i in range(len(m)):
            if m[i] == '1':
                if prev != -1:
                    gap = max(gap, i - prev)
                prev = i
        return gap
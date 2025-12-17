class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fb,fs,sb,ss = -10**60,0,-10**60,0

        for i in prices:
            fb = max(fb, -i)
            fs = max(fs, fb+i)
            sb = max(sb, fs-i)
            ss = max(ss, sb+i)
        return ss
        
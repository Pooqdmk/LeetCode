class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        suf = [0]*(n+1)

        for i in range(n-1,-1,-1):
            suf[i] = max(suf[i+1],events[i][-1])
        
        val = [s for s,e,v in events]
        mx = 0
        for s,e,v in events:
            idx = bisect_right(val,e)

            mx =max(mx,v + suf[idx])
        return mx


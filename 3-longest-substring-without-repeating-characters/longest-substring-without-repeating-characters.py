class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        seen = set(queue)
        mx = 0
        for i in range(len(s)):
            while queue and s[i] in seen:
                mx = max(mx,len(queue))
                seen.remove(queue.popleft())
            queue.append(s[i])
            seen.add(s[i])
        return max(mx,len(queue))
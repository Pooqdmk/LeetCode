class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = deque()
        seen = set(stack)
        mx = 0
        for i in range(len(s)):
            while stack and s[i] in seen:
                mx = max(mx,len(stack))
                seen.remove(stack.popleft())
            stack.append(s[i])
            seen.add(s[i])
        return max(mx,len(stack))
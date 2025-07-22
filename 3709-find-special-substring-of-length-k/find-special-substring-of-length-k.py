class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n=len(s)
        for i in range(n-k+1):
            l=s[i:i+k]
            if len(set(l)) == 1:
                left=i-1
                right=i+k

                if (left>=0 and s[left]!=s[i] and right>=n) or (left>=0 and s[left]!=s[i] and right<n and s[right]!=s[i]) or (left<0 and right<n and s[right]!=s[i]) or (left<0 and right>=n):
                    return True

        return False
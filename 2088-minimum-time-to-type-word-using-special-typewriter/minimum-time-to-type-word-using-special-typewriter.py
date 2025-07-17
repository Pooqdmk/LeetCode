class Solution:
    def minTimeToType(self, word: str) -> int:
        cnt=0
        cur='a'
        for i in word:
            diff=abs(ord(i)-ord(cur))
            cnt+=min(diff,26-diff)+1
            cur=i
        return cnt
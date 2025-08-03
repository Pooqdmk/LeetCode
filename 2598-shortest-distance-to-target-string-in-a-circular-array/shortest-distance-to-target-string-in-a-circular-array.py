class Solution:
    def closestTarget(self, words: List[str], target: str, st: int) -> int:
        if target not in words:
            return -1
        
        n=len(words)
        mn=10**6
        for i in range(n):
            if words[i]==target:
                mn=min(mn,min(abs(st-i),n-abs(st-i)))
        return mn 
        
    

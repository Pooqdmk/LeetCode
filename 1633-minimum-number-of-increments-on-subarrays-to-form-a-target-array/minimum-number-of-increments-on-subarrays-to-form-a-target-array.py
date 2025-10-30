class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]

        for i in range(1,len(target)):
            diff = target[i] - target[i-1]
            if diff > 0:
                res+= diff
        return res
            

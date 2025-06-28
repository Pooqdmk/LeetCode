class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = list(enumerate(nums))
        s=sorted(indexed,key=lambda x:x[1] ,reverse=True)[:k]

        r=sorted(s,key=lambda x :x[0])

        return [i[1] for i in r]

        


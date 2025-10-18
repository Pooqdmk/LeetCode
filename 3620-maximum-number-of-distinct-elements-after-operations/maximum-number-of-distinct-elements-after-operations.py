class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        prev= -math.inf
        for i in nums:
            curr = max(prev+1,i-k)

            if curr <= i+k:
                cnt+=1
                prev = curr 
        return cnt
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            n = nums[i:i+k]
            d = Counter(n)
            l = sorted(d.items(), key = lambda x:(x[1],x[0]),reverse = True)
            res.append(sum(k*v for k,v in l[:x]))

        return res

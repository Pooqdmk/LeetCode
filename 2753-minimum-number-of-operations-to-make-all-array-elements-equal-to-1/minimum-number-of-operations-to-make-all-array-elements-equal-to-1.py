class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        n = len(nums)
        if ones > 0:
            return n - ones
        mn = 10**60
        for i in range(n):
            a = nums[i]
            for j in range(i+1,n):
                a = gcd(a,nums[j])
                if a == 1:
                    mn = min(mn,j-i+1)
                    break
        return (n-1) + (mn-1) if mn != 10**60 else -1
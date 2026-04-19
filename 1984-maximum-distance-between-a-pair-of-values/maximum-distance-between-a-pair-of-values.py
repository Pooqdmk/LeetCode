class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        mx = -10**60
        for i in range(len(nums1)):
            mx = max(mx, bisect.bisect_right(nums2,-nums1[i], key = lambda x:-x)-i-1)
        return mx if mx > -1 else 0
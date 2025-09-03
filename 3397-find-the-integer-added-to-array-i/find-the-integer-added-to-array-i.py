class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = min(nums1),min(nums2)
        return n-m
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums1).intersection(set(nums2))
        if len(s)>=1:
            return min(s)
        else:
            a=str(min(nums1))
            b=str(min(nums2))
            i=int(a + b)
            j=int(b+a)
            return i if i<j else j

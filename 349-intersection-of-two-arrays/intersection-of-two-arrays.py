class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1) 
        r=set(nums2)
        l=[]
        for i in nums1:
            if i in s and i in r and i not in l:
                l.append(i)
        return l
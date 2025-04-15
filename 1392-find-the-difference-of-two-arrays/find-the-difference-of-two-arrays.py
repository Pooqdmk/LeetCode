class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li=[]
        li.append(list(set(nums1) - set(nums2)))
        li.append(list(set(nums2)-set(nums1)))
        return li
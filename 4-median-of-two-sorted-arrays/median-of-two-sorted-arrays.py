class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # a = []
        # n,m = len(nums1),len(nums2)
        # i,j = 0,0
        # while i < n and j<m:
        #     if nums1[i] < nums2[j]:
        #         a.append(nums1[i])
        #         i+=1
        #     else:
        #         a.append(nums2[j])
        #         j+=1
        # while i < n:
        #     a.append(nums1[i])
        #     i+=1
        # while j < m:
        #     a.append(nums2[j])
        #     j+=1

        # if (n+m) % 2 == 0:
        #     mid = (m+n) // 2
        #     return (a[mid] + a[mid-1]) / 2
        # else:
        #     return a[(n+m)//2]
        
        a = sorted(nums1 + nums2)
        n=len(a)
        mid = n//2
        if n%2 == 0:
            return (a[mid]+a[mid-1]) / 2
        else:
            return a[mid]
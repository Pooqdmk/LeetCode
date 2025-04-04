class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        
        for i in nums1:
            app=False
            ind=nums2.index(i)
            for j in range(ind+1,len(nums2)):
                if nums2[j]>i:
                    app=True
                    li.append(nums2[j])
                    break
            if app==False:
                li.append(-1)
        return li

            
            
            
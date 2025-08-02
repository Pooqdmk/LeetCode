class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={i[0]:i[1] for i in nums1}
        l={i[0]:i[1] for i in nums2}

        nums=list(set([i[0] for i in nums1] + [i[0] for i in nums2]))
        res={}
        for i in nums:
            if i in d and i in l:
                res[i]=d[i]+l[i]
            elif i in d:
                res[i]=d[i]
            else:
                res[i]=l[i]
        
        res=list(sorted(res.items(),key=lambda x:x[0]))
        for i in range(len(res)):
            res[i]=list(res[i])
        return res
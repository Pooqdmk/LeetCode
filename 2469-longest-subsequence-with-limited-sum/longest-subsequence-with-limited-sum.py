class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        l=[]
        for i in range(len(queries)):
            res=[]
            # res.append(0)
            s=0
            for j in nums:
                if s+j <= queries[i]:
                    s+=j
                    res.append(j)
                else:
                    l.append(len(res))
                    break
            if len(res) == len(nums):

                l.append(len(res))

        return l



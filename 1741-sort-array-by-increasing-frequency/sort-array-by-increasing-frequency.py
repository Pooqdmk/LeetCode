class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=Counter(nums)

        # s=sorted(d.items(),key=lambda x:x[1])
        # res=[]
        # for i in s:
        #     res.append([i[0]]*i[1])
        # return sum(res,[])
        nums.sort(key=lambda x:(d[x],-x))
        return nums
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list)
        l = {}
        for i in range(len(nums)):
            d[nums[i]].append(i)
            l[nums[i]] = l.get(nums[i],0)+1
        global_mn = 10**60
        for k,v in l.items():
            if v >= 3:
                mn = 10**60
                for i in range(len(d[k])-2):
                    mn = min(mn,abs(d[k][i] - d[k][i+1]) + abs(d[k][i+1] - d[k][i+2]) + abs(d[k][i] - d[k][i+2]))
                global_mn = min(global_mn, mn)
        return global_mn if global_mn!=10**60 else -1

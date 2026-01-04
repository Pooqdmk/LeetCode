class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def valid(i):
            s = 0
            cnt = 0
            for j in range(1,int(sqrt(i))+1):
                if i%j == 0:
                    cnt+=1
                    s+=j
                    if j*j != i:
                        cnt+=1
                        s+=(i//j)
                if cnt > 4:
                    break
            if cnt == 4:
                return s
            else:
                return 0


        res = 0
        for i in nums:
            res+=valid(i)
        return res


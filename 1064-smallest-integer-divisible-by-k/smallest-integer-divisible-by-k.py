class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        d = set()
        i = 1
        cnt = 1
        while True:
            if i%k == 0:
                return cnt
            if i%k not in d:
                d.add(i%k)
            else:
                break
            i=i*10 + 1
            cnt+=1
        return -1


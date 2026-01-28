class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)

        def helper(first,sec,rem):
            if len(rem) < max(len(first), len(sec)):
                return False
            if (first[0] == '0' and len(first) > 1) or (sec[0] == '0' and len(sec) > 1):
                return False
            res = str(int(first) + int(sec))
            if res == rem:
                return True
            if rem.startswith(res):
                first = sec
                sec = res
                rem = rem[len(res):]
                return helper(first,sec,rem)
            

        i = 0
        for j in range(i+1, n):
            for k in range(j+1,n):
                first = num[i:j]
                sec = num[j:k]
                rem = num[k:]
                if helper(first,sec,rem):
                    return True
        return False

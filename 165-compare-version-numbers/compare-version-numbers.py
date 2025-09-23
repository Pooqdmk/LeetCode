class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        l1,l2=len(v1),len(v2)
        mx = max(l1,l2)
        for i in range(mx):
            if i >= l1:
                v1.append('0')
            if i >= l2:
                v2.append('0')
            
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0
                
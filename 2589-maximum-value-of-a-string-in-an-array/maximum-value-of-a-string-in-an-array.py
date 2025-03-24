class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m=0
        for i in strs:
            if i.isalnum() and not (i.isdigit()):
                if m<len(i):
                    m=len(i)
            else:
                if m<int(i):
                    m=int(i)
        return m
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # cnt=0
        # for i in details:
        #     if int(i[12:14])>60:
        #         cnt=cnt+1
        # return cnt
        return sum(1 for i in details if int(i[11:13])>60)
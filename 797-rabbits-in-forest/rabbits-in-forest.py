class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt=0
        d=Counter(answers)
        for key,val in d.items():
            grp_size=key+1
            grp=math.ceil(val/grp_size)
            cnt+=grp*grp_size
        return cnt
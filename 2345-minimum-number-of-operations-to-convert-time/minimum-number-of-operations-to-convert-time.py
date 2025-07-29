class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_mn=int(current[:2])*60 + int(current[3:])
        corr_mn=int(correct[:2])*60 + int(correct[3:])
        minutes=corr_mn - curr_mn
        cnt=0
        
        if minutes>=60:
            cnt+=(minutes//60)
            minutes-=(minutes//60)*60
            
        if minutes>=15:
            cnt+=(minutes//15)
            minutes-=(minutes//15)*15
            
        if minutes>=5:
            cnt+=(minutes//5)
            minutes-=(minutes//5)*5
            
        if minutes>=1:
            cnt+=(minutes//1)
            minutes-=(minutes//1)*1
            
        return cnt

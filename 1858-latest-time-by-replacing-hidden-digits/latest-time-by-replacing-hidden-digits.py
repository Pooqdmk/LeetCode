class Solution:
    def maximumTime(self, time: str) -> str:
        time=list(time)
        if time[0]=='?':
            if time[1]=='?' or time[1]<='3':
                time[0]='2'
            else:
                time[0]='1'

        if time[1]=='?':
            if time[0]=='2':
                time[1]='3'
            else:
                time[1]='9'
        
        if time[-2]=='?':
            time[-2]='5'
        
        if time[-1]=='?':
            time[-1]='9'

        return ''.join(time)
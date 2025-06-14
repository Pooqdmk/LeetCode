class Solution:
    def reformatDate(self, date: str) -> str:
        d={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        l=date.split(' ')
        day=''
        for i in l[0]:
            if i.isdigit():
                day+=i
        if len(day)==1:
            day='0'+day
        return l[-1]+"-"+d[l[1]]+"-"+day


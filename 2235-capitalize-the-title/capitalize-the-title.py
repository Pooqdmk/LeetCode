class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res=''
        l=title.split()
        for i in l:
            if len(i) <=2:
                res+=i.lower()+' '
            else:
                res+=i[0].upper()+i[1:].lower()+' '

        return res.rstrip()
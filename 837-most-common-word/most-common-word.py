class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c=re.sub(r'[^\w]',' ',paragraph.lower())
        l=Counter(c.split())
        for i,f in l.most_common():
            if i not in banned:
                return i
        return ""

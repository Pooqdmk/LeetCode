class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        d={chr(i+ord('a')):morse_codes[i] for i in range(26)}
        l=[]
        for i in words:
            s=''
            for j in i:
                s=s+d[j]
            l.append(s)
        return len(set(l))

        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = len,reverse = True)
        res = [words[0]]

        for i in range(1,len(words)):
            found = False
            for j in res:
                if j.endswith(words[i]):
                    found = True
                    break

            if not found: 
                res.append(words[i])
        # print('#'.join(res))
        return len('#'.join(res))+1
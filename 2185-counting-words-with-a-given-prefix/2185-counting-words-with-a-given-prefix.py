class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count=0
        for i in range(len(words)):
            if len(words[i])<len(pref):
                continue
            n=len(words[i])
            m=len(pref)
            j=0
            while j<m:
                if words[i][j]==pref[j]:
                    j+=1
                else:
                    break
            if j==m:
                count+=1
        return count
        
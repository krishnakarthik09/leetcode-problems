class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n=len(s)
        Xor=0
        j=0
        for i in range(len(t)):
            if i<n:
                Xor=Xor^ord(s[i])
            Xor=Xor^ord(t[j])
            j+=1
        return chr(Xor)
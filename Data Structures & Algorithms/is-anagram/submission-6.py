class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS = {}
        CountT = {}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            harfS = s[i]
            CountS[harfS] = 1 + CountS.get(harfS, 0)

            harfT = t[i]
            CountT[harfT] = 1 + CountT.get(harfT, 0)
        
        return CountS == CountT
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            chS = s[i]
            countS[chS] = 1 + countS.get(chS, 0)

            chT = t[i]
            countT[chT] = 1 + countT.get(chT, 0)

        return countT == countS
        
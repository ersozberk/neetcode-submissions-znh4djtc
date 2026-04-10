class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}

        for i in range(len(s)):
            charS = s[i]
            dictS[charS] = 1 + dictS.get(charS, 0)

            charT = t[i]
            dictT[charT] = 1 + dictT.get(charT, 0)
        

        return dictS == dictT


        
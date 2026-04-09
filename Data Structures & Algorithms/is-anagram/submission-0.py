class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        countS={}
        countT={}
        
        for i in range(len(s)):
            harfS = s[i]
            countS[harfS]=1+countS.get(harfS, 0)

            harfT = t[i]
            countT[harfT]=1+countT.get(harfT, 0)
        
        return countS == countT
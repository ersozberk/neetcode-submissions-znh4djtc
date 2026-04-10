from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for s in strs:
            # Her kelime için a'dan z'ye 26 karakterlik sayacı sıfırla
            count = [0] * 26 
            
            for char in s:
                # Karakterin ASCII değerine göre indeksini bul (a=0, b=1...)
                count[ord(char) - ord('a')] += 1
            
            # Listeler hashlenemez, bu yüzden tuple'a çevirip anahtar yapıyoruz
            res[tuple(count)].append(s)
        
        return list(res.values())
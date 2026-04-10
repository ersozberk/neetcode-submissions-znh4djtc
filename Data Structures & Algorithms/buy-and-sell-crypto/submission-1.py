class Solution:
    def maxProfit(self, prices: List) -> int:
        min_price = float('inf')  # Karşılaştırma yapabilmek için başlangıçta sonsuz yapıyoruz
        max_profit = 0            # Hiç kâr yoksa 0 döndüreceğiz
        
        for price in prices:
            # Soru 1: Daha ucuz bir alım fırsatı bulduk mu?
            if price < min_price:
                min_price = price
                
            # Soru 2: Bugün satsam, kâr rekoru kırar mıyım?
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            mevcut_sayi = nums[i]
            aranan_sayi = target - mevcut_sayi

            if aranan_sayi in seen:
                return [seen[aranan_sayi], i]
            
            seen[mevcut_sayi] = i
        



        
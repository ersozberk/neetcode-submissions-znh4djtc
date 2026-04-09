class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gorulenler = {}

        for i in range(len(nums)):
            mevcut_sayi=nums[i]
            aranan_sayi = target - mevcut_sayi

            if aranan_sayi in gorulenler:
                return [gorulenler[aranan_sayi], i]
            gorulenler[mevcut_sayi]=i
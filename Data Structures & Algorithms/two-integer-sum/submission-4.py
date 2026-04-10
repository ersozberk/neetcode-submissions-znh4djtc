class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            mevcut = nums[i]
            aranan = target - mevcut

            if aranan in seen:
                return [seen[aranan], i]
            
            seen[mevcut] = i
        
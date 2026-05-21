class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, j in enumerate(nums):
            if target - j in seen:
                return [seen[target-j], i]
            else:
                seen[j] = i
        

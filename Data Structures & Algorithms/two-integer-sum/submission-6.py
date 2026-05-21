class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i , n in enumerate(nums):
            req = target - n

            if req in seen.keys():
                return [seen[req] , i]
            else:
                seen[n] = i
        return seen

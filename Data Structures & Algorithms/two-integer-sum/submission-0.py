class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, j  in enumerate(nums):
            if (target - j) in nums and (nums.index(target-j) != i):
                if i < nums.index(target-j):
                    return [i,nums.index(target-j)]
                return [nums.index(target-j), i]


        
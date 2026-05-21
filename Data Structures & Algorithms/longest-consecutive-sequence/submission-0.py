class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                length= 0
                while (nums[i] +length in numset ) :
                    length +=1
                longest = max(longest, length)
        return longest


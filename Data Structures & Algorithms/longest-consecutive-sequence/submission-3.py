class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums) #remove all dupes and gives us constant time lookups
        for i in range(len(nums)):
            #check if the number we are at does not have a prev num in the set
            #if so then we are at the first num in a subsequence
            if nums[i] - 1 not in numset:
                length= 0
                while (nums[i]+length in numset ) :
                    length +=1
                longest = max(longest, length)
                # if length>longest:
                #     longest = length
        return longest


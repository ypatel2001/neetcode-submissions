class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        #sorting helps us turn this into a 2 sum II similar problem 
        # and use pointers to compare the current sum to tho 0 once 
        # we have our first number 
        nums.sort()

        for i , a in enumerate(nums):
            # we dont want anything over a 0 so we can skip to next 
            if a > 0:
                break 
            # avoid dupe triplets
            if i> 0 and a == nums[i-1]:
                continue 

            #i + 1 because we need to skip forward 1 as we have value A at index 1 
            l = i + 1 
            r = len(nums)-1
            while l < r: 
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r : 
            # we need to do l + ((r-l)//2) to avoid buffer overflow
            m = l + ((r-l)//2) 
            #m = (l + r ) // 2 # get rough midpoint to bisect array
            if nums[m] < target: 
                l = m + 1
            elif nums[m] > target : 
                r = m - 1
            else:
                return m
        return -1

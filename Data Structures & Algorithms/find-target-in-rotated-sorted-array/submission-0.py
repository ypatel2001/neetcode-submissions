class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Why Check Which Half is Sorted?
# We use binary search, but since the array is rotated, we must:
# Find which half (left or right) is still sorted (unbroken by rotation).
# Check if target is in that sorted half → If yes, search there. Else, search the other half.
         
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # early terminator statement 
            if target == nums[mid]:
                return mid

            #check if its in the left sorted array 
            if nums[l] <= nums[mid]:
             #If left is sorted and target is in [nums[l], nums[mid]), search left. Else, search right.
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # check if its in right array   
            else:
                #If right is sorted and target is in (nums[mid], nums[r]], search right. Else, search left.
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
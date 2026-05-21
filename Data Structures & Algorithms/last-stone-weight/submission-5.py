import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-s for s in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            first = -1 * heapq.heappop(nums)
            second = -1 * heapq.heappop(nums)

            diff = abs(second - first) # If first was the largest, diff will be negative or zero
            if diff > 0:
                heapq.heappush(nums, -diff) # You want to push the positive difference back

        nums.append(0) # This line seems unnecessary for the logic
        return abs(nums[0]) # If the loop finishes with one element, it's the last weight.
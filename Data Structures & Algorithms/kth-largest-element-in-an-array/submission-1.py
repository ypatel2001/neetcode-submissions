class Solution:
    def findKthLargest(self, nums, k):
        #return heapq.nlargest(k, nums)[-1]
        heapq.heapify(nums)
        while len(nums) > k-1:
            popped = heapq.heappop(nums)
        return popped
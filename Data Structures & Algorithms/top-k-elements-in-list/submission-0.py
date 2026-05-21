class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen= defaultdict(int)
        frequency = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num] = 1
        
        for num, count in seen.items():
            frequency[count].append(num)

        result = []

        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                result.append(j)
            if len(result) == k:
                return result

        
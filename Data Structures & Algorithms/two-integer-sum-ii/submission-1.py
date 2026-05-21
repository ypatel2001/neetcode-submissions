class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      l = 0 
      r = len(numbers) - 1

      while l < r : 
        currentSum = numbers[l] + numbers[r]
        
        if currentSum < target:
            l+=1
        
        elif currentSum > target:
            r-=1

        else: 
            # the indexes returned need to be one indexed 
            #as per the problem instructions
            return [l + 1 , r + 1]


        


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Normal soln
        # make a dict and output var
        count = {}
        res = 0 

        l = 0 
        #loop thrs s and and update the freq count of the letter at right pointer
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

        #while window size - max of freqs in dict > k
        # we decrement count of left pointer letter by 1 and move up left pointer
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
        #update result to the max of current result vs current window size
            res = max(res, r - l + 1)
        return res

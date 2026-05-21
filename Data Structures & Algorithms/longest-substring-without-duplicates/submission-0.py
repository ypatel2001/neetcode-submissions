class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to hold unique letters in substring
        seen = set()
        #init left at 0 and max to 0 as default value
        l = 0 
        maxlength = 0

        # new way: right is init and used from this for loop 
        for r in range(len(s)):
            #while we have any dupes, we pop the leftmost value to shorten window 
            #and slide it forward but incrementing L
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            # if not then we just add the rightmost char
            # and R gets incremented via the for loop
            seen.add(s[r])
            #update the max length , we get the longest sub length by doing R- L + 1 
            # this is because of arrays being 0 indexed
            # len() gives the 1 indexed value, 
            maxlength = max(maxlength, r -l + 1)
        return maxlength
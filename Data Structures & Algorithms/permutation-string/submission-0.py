class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s1 can't be a permutation of any substring of s2
        if len(s1) > len(s2):
            return False
        
        # Create frequency count arrays for characters in s1 and for the first window in s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Calculate how many characters match in frequency between s1Count and s2Count
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0  # Left pointer of the sliding window
        for r in range(len(s1), len(s2)):  # r expands the window over s2
            if matches == 26:  # If all character counts match, we found a permutation
                return True
            
            # Expand the window by adding the rightmost character
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:  # If counts match after adding, increment matches
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # If it was matching before and now it's off, decrement
                matches -= 1

            # Shrink the window by removing the leftmost character
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:  # If counts match after removing, increment matches
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  # If it was matching before and now it's off, decrement
                matches -= 1
            l += 1  # Move the left pointer to keep the window size fixed

        # Final check in case the last window matches
        return matches == 26

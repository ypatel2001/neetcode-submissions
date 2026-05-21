class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make left and right pointers and length
        #need to use .lower() to make all chars lowercase 
        l = 0 
        r = len(s) - 1  # need to minus 1 to avoid out of bounds error

        # checking while the pointers have not met in the middle
        while l < r: 
            #checking that the pointers havent met 
            #and that the char is NOT alphanum, we move the pointers along
            #until the pointers are at valid chars that we can compare
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # check if the chars do not match, return false 
            #else increment the pointers until the phrase is done
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True
            

         #checks if char is alphanumeric 

    def alphaNum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))



       
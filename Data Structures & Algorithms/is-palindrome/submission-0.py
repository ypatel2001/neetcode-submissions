class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make left and right pointers and length
        #need to use .lower() to make all chars lowercase 
        l = 0 
        r = 0 
        length = len(s)

        output = ''

        for i in s:
            if i.isalnum():
                output += i.lower()
        return output == output[::-1]



       
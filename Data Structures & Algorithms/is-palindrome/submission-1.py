class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cheating solution but very fast to implement 
        output = ''

        for i in s:
            if i.isalnum():
                output += i.lower()
        return output == output[::-1]



       
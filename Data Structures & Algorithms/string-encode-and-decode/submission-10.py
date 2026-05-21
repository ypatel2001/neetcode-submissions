class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ''
        for string in strs:
            output +=  str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0 

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            output.append(s[j+1 : j+1+length])
            i = j+1+length


        return output
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''

        if len(strs) == 0:
            return "empty"
        for i in range(len(strs)):
        
            if  i == 0:
                result = result + (strs[i])
                continue
            result = result + ("?" +strs[i])
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split("?")

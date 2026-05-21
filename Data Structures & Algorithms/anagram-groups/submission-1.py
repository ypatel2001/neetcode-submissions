class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            #cannot have a dict as the key so we use the fact that
            #alphabet only has 26 letter to make a makeshift dict 
            alphabet_count = [0] * 26

            for i in word:
                #get the index to change using ord and - ord('a')
                #then increment by 1
                alphabet_count[ord(i) - ord('a')] += 1
            
            if tuple(alphabet_count) not in seen.keys():
                seen[tuple(alphabet_count)] = []
           
            seen[tuple(alphabet_count)].append(word)
                

        return seen.values()


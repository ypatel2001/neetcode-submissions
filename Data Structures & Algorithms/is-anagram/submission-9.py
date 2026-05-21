class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sDict = {}
        # tDict = {}

        # for i in s:
        #     sDict[i] = sDict.get(i, 0) + 1
        # for j in t:
        #     tDict[j] = tDict.get(j, 0) + 1
        # return tDict == sDict

        sDict = {}
        tDict = {}

        for i in s: 
            sDict[i] = sDict.get(i, 0) + 1 
        for j in t:
            tDict[j] = tDict.get(j, 0) + 1 
        return tDict == sDict
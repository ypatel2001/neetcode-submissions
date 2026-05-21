class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        dict_s , dict_t = {}, {}

        for i in s:
            if i not in dict_s.keys():
                dict_s[i] = 1
            dict_s[i] = dict_s[i]+1
        for j in t:
            if j not in dict_t.keys():
                dict_t[j] = 1
            dict_t[j] = dict_t[j]+1
        
        return dict_s == dict_t
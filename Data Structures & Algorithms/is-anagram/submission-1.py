class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in s:
            if i not in dict_s.keys():
                dict_s[i]=1
            dict_s[i] = dict_s[i] + 1
        
        dict_t = {}
        for j in t:
            if j not in dict_t.keys():
                dict_t[j]=1
            dict_t[j] = dict_t[j] + 1

        if dict_s == dict_t:
            return True
        if dict_s != dict_t:
            return False
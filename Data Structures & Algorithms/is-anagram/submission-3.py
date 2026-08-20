class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}

        for i in range(len(s)):
            if s[i] in dicts:
                dicts[s[i]]+=1
            else:
                dicts[s[i]]=1
            
        for c in range(len(t)):
            if t[c]in dictt:
                dictt[t[c]]+=1
            else:
                dictt[t[c]]=1
           

        if dictt==dicts:
            return True
        return False
            
        
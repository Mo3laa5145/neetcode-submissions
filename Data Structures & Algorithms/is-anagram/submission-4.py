class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        

        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
            
        for c in range(len(t)):
            if t[c]in dict:
                dict[t[c]]-=1
            else:
                dict[t[c]]= -1
           

        for value in dict.values():
            if value != 0:
                return False
        else:
            return True

                        
        
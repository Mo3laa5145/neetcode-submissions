class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0
        s = s.lower()

        while right>left:
            if not s[right].isalnum():
                right-=1
            elif not s[left].isalnum():
                left +=1
            elif s[left] == s[right] :
                right-=1
                left+=1
            else:
                return False
        return True